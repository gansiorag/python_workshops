# Этот код представляет собой набор низкоуровневых утилит для потоковой
# (ленивой) обработки бинарных данных. Главная особенность здесь — работа 
# с итераторами и генераторами (yield). Данные не загружаются в память целиком, 
# а обрабатываются небольшими порциями (чанками),
# что позволяет эффективно работать с файлами любого размера.

import io
import zlib
from gzip import GzipFile
from typing import AnyStr, Iterator, Optional


def gzip_stream(f: io.IOBase, chunk_size: int = io.DEFAULT_BUFFER_SIZE):
    """Генератор для потоковой распаковки GZIP-данных на лету.
    Что делает: Принимает уже открытый сжатый файл или сетевой поток f и 
    выдает его содержимое декомпрессованным кусками.
    Как работает: Оборачивает входной файловый объект f в стандартный 
    библиотечный класс GzipFile (переменная gfh). Затем делегирует чтение 
    этому обертке внутри функции file_stream. Оператор yield from прозрачно 
    передает чанки распакованных данных потребителю.
    Зачем нужно: Распаковка происходит инкрементально. Библиотека gzip держит 
    во внутреннем буфере только необходимый минимум данных для алгоритма сжатия, 
    поэтому потребление памяти остается низким даже при обработке
    многогигабайтных архивов.

    Args:
        f (io.IOBase): _description_
        chunk_size (int, optional): _description_. Defaults to io.DEFAULT_BUFFER_SIZE.

    Yields:
        _type_: _description_
    """

    with GzipFile(fileobj=f) as gfh:
        yield from file_stream(gfh, chunk_size)


def file_stream(f: io.IOBase, chunk_size: int = io.DEFAULT_BUFFER_SIZE):
    """Это базовый генератор-итератор «сырого» чтения файла.
    Что делает: Читает данные из переданного файлового объекта f блоками по 
    chunk_size байт до тех пор, пока файл не закончится.
    Как работает: В бесконечном цикле вызывается метод .read(chunk_size).
    Если возвращается пустой байтовый объект b"", это сигнал конца файла (EOF),
    цикл прерывается. Иначе полученный кусок данных отдается через yield.
    
    Зачем нужно: Позволяет читать огромные файлы без риска переполнить
    оперативную память. Это фундаментальный кирпичик для всех остальных функций потока.

    Args:
        f (io.IOBase): _description_
        chunk_size (int, optional): _description_. Defaults to io.DEFAULT_BUFFER_SIZE.

    Yields:
        _type_: _description_
    """

    while True:
        chunk = f.read(chunk_size)
        if chunk == b"":
            break
        yield chunk


def iter_lines(data: Iterator[AnyStr], keep_ends: bool = False) -> Iterator[AnyStr]:
    """
    Разделитель сплошного потока байтов или строк на отдельные строки.
    Что делает: Собирает произвольные куски данных (которые могут приходить как угодно —
    например, посередине строки) и корректно разбивает их на полные строки.
    
    Как работает:
    Использует переменную-аккумулятор pending, куда склеиваются пришедшие чанки.
    Метод .splitlines(True) делит накопленный текст на список строк, сохраняя символы
    переноса строки (\n, \r\n) благодаря флагу True.
    Все готовые строки (кроме последней неполной) сразу выдаются через yield. Последняя
    часть сохраняется обратно в pending в ожидании следующего чанка.
    После окончания цикла проверяется остаток в pending и выдается последняя строка.
    Параметр keep_ends управляет тем, будут ли сохранены символы перевода строки в
    итоговых строках.

    Зачем нужно: Стандартный метод .readline() плохо дружит со стримингом больших объемов,
    так как часто читает слишком маленькие порции. Эта функция решает проблему
    "разрезанных" строк при чтении большими блоками.

    Args:
        data (Iterator[AnyStr]): _description_
        keep_ends (bool, optional): _description_. Defaults to False.

    Yields:
        Iterator[AnyStr]: _description_
    """    
    pending = b""
    for chunk in data:
        pending += chunk

        lines = pending.splitlines(True)
        if not lines:
            continue

        for line in lines[:-1]:
            yield line.splitlines(keep_ends)[0]
        pending = lines[-1]

    if pending:
        yield pending.splitlines(keep_ends)[0]


def iter_decompress(
    data: Iterator[bytes], encoding: Optional[str] = None
) -> Iterator[bytes]:
    """
    Универсальный декомпрессор для сырых потоков байтов (не файлов).

    Что делает: Декомпрессирует поток байтов data, используя алгоритм zlib/deflate/gzip
    напрямую, минуя работу с заголовками файлов.

    Как работает:
    Если encoding=None, функция просто пропускает данные сквозь себя (yield from data),
    работая как заглушка. Определяет режим работы библиотеки zlib через параметр wbits.
    Значение 16 + zlib.MAX_WBITS включает обработку gzip-заголовков, а обычное
    zlib.MAX_WBITS — чистый deflate. Создает объект-декомпрессор zlib.decompressobj.
    Внутри цикла принимает каждый чанк, прогоняет его через decompressor.decompress().
    Объект сам следит за состоянием алгоритма между вызовами.
    Особая логика дефейта (Deflate): Проверка chunk[0] & 0xF != 8 определяет валидность
    заголовка zlib. Если он некорректен, библиотека переключается в
    режим wbits=-zlib.MAX_WBITS ("raw deflate"), который игнорирует любые служебные
    поля и пытается извлечь чистые сжатые блоки. Это частое решение для совместимости
    с данными, которые были сжаты нестандартными инструментами.
    В конце вызывает decompressor.flush(), чтобы забрать остатки данных из внутренних
    буферов алгоритма.

    Зачем нужно: Используется, когда данные приходят по сети (например, HTTP-ответы с
    Content-Encoding: gzip или deflate) или хранятся в специфических форматах, где нет
    полноценного .gz-файла, но есть полезная нагрузка, упакованная этими алгоритмами.

    Args:
        data (Iterator[bytes]): _description_
        encoding (Optional[str], optional): _description_. Defaults to None.

    Yields:
        Iterator[bytes]: _description_
    """    
    if encoding is None:
        yield from data

    zlib_mode = 16 + zlib.MAX_WBITS if encoding == "gzip" else zlib.MAX_WBITS
    decompressor = zlib.decompressobj(wbits=zlib_mode)

    decode_started = False
    for chunk in data:
        if not decode_started and encoding == "deflate" and chunk[0] & 0xF != 8:
            # Change the decoder to decompress incorrectly compressed data
            # Actually we should issue a warning about non-RFC-compliant data.
            decompressor = zlib.decompressobj(wbits=-zlib.MAX_WBITS)

        decompressed_chunk = decompressor.decompress(chunk)
        decode_started = True
        if decompressed_chunk != b"":
            yield decompressed_chunk

    decompressed_chunk = decompressor.flush()
    if decompressed_chunk != b"":
        yield decompressed_chunk


# Работа функций вместе
if __name__ == '__main__':

    with open("huge_log.gz", "rb") as f:
        # 1. Потоковое чтение сырого файла кусками -> file_stream()
        raw_chunks = file_stream(f)

        # 2. Потоковая распаковка GZIP -> gzip_stream()
        decompressed_bytes = gzip_stream(raw_chunks)

        # 3. Разбиение на строки -> iter_lines()
        lines = iter_lines(decompressed_bytes)

        for line in lines:
            if b"ERROR" in line:
                print(line.decode('utf-8'))

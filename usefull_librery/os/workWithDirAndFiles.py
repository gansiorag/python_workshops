'''
 This module make 
    
Athor: Gansior Alexander, gansior@gansior.ru, +79173383804
Starting 2022//
Ending 2022//
    
'''
    
from termcolor import cprint
import inspect
'''
Text colors: grey red green yellow blue magenta cyan white
Text highlights: on_grey on_red on_green on_yellow on_blue on_magenta on_cyan on_white
Attributes: bold dark underline blink reverse concealed
template --> cprint(f'{}' , 'red', attrs=['bold'])
    
    
Shows which module is currently running
cprint('='*20 + ' >> ' + inspect.stack()[0][0].f_code.co_name + ' << '+'='*20, 'red', attrs=['bold'])
'''
import os    
    
def Path1():
    cprint('='*20 + ' >> ' + inspect.stack()[0][0].f_code.co_name + ' << '+'='*20, 'red', attrs=['bold'])
    print("Текущая деректория:", os.getcwd())
    
    os.chdir('D:/Project_My/python_workshops/usefull_librery/os')
    # вывод текущей папки
    cprint(f"Текущая директория изменилась на folder: {os.getcwd()}", 'blue')
    
    # создать пустой каталог (папку)
    #os.mkdir("folder")
    # повторный запуск mkdir с тем же именем вызывает FileExistsError, 
    # вместо этого запустите:
    if not os.path.isdir("folder"):
        os.mkdir("folder")
    
    # изменение текущего каталога на 'folder'
    os.chdir("folder")
    # вывод текущей папки
    cprint(f"Текущая директория изменилась на folder: {os.getcwd()}", 'blue')
    
    # вернуться в предыдущую директорию
    os.chdir("..")

    # сделать несколько вложенных папок
    if not os.path.isdir("nested1/nested2/nested3"):
        os.makedirs("nested1/nested2/nested3")
    
    # удалить папку
    os.rmdir("folder")
    
    # удалить вложенные папки
    os.removedirs("nested1/nested2/nested3") 
    
    # walk Рекурсивное получение имен файлов в дереве каталогов.
    # Функция walk() модуля os генерирует имена файлов в дереве каталогов, обходя дерево 
    # сверху вниз или снизу вверх. Для каждого каталога в дереве с корнем в вершине каталога top, 
    # включая саму вершину top, она выдает тройной кортеж (dirpath, dirnames, filenames).
    # dirpath - это строка, путь к каталогу.
    # dirnames - это список имен подкаталогов в dirpath, исключая особые символы '.' и '..'.
    # filenames - это список имен файлов в dirpath (не-каталогов).
    # top - строка, вершинa каталога,
    # topdown=True - bool, направление обхода,
    # onerror=None - функция, которая сообщает об ошибке,
    # followlinks=False - bool, переходить ли по символическим ссылкам.
    
    top= os.getcwd()
    top = top.replace(top.split('\\')[-1],'')
    print(top)
    rez = os.walk(top, topdown=True, onerror=None, followlinks=False)
    for dd in rez:
        cprint(dd, 'blue')
        print()
    
    # os.unlink() method in Python is used to remove or delete a file path
    
    
def Path2():
    os.chdir('D:/Project_My/python_workshops/usefull_librery/os')
    if not os.path.isdir("folder"):
        os.mkdir("folder")
    # вывод текущей папки
    cprint(f"Текущая директория изменилась на folder: {os.getcwd()}", 'blue')
    
    # создать новый текстовый файл
    text_file = open("text.txt", "w")
    
    # запить текста в этот файл
    text_file.write("Это текстовый файл")
    text_file.close()
    
    # вывести некоторые данные о файле
    # st_size — размер файла в байтах
    # st_atime — время последнего доступа в секундах (временная метка)
    # st_mtime — время последнего изменения
    # st_ctime — в Windows это время создания файла, а в Linux — последнего изменения метаданных
    print(os.stat("text.txt"))
    
    # переименовать text.txt на renamed-text.txt
    os.rename("text.txt", "renamed-text.txt")       
    
    # заменить (переместить) этот файл в другой каталог
    os.replace("renamed-text.txt", "folder/renamed-text.txt")
    
    # распечатать все файлы и папки в текущем каталоге
    print("Все папки и файлы:", os.listdir())
    
    # распечатать все файлы и папки рекурсивно
    # os.walk() — это генератор дерева каталогов. Он будет перебирать все переданные составляющие. 
    # Здесь в качестве аргумента передано значение «.», которое обозначает верхушку дерева
    for dirpath, dirnames, filenames in os.walk("."):
        # перебрать каталоги
        for dirname in dirnames:
            print("Каталог:", os.path.join(dirpath, dirname))
        # перебрать файлы
        for filename in filenames:
            print("Файл:", os.path.join(dirpath, filename))
    # удалить этот файл
    os.remove("folder/renamed-text.txt")
    
if __name__ == '__main__':
    name=''
    Path1()
    #Path2()
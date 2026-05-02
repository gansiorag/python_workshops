import xml.etree.ElementTree as ET
from typing import Any, Dict, List
from pprint import pprint
from datetime import datetime


def parse_xml_full(xml_file_path: str) -> Dict[str, Any]:
    """
    Полный парсинг XML файла с рекурсивным обходом всех элементов.
    
    Args:
        xml_file_path: Путь к XML файлу
        
    Returns:
        Словарь со всей структурой данных
    """
    
    def parse_element(element: ET.Element, depth: int = 0) -> Dict[str, Any]:
        """
        Рекурсивный парсинг элемента XML.
        
        Args:
            element: XML элемент для парсинга
            depth: Текущая глубина вложенности
            
        Returns:
            Словарь с данными элемента
        """
        result = {
            'tag': element.tag,
            'attributes': dict(element.attrib),
            'text': element.text.strip() if element.text and element.text.strip() else None,
            'children': []
        }
        
        # Рекурсивно обрабатываем всех дочерних элементов
        for child in element:
            result['children'].append(parse_element(child, depth + 1))
        
        return result
    
    # Читаем XML файл
    tree = ET.parse(xml_file_path)
    root = tree.getroot()
    
    # Парсим корневой элемент
    parsed_data = parse_element(root)
    
    return parsed_data


def print_xml_structure(data: Dict[str, Any], indent: int = 0, max_depth: int = None):
    """
    Красивый вывод структуры XML с отступами.
    
    Args:
        data: Словарь с данными от parse_element
        indent: Текущий отступ
        max_depth: Максимальная глубина вывода (None - без ограничений)
    """
    current_depth = indent // 2
    
    if max_depth is not None and current_depth > max_depth:
        return
    
    prefix = "  " * current_depth
    
    # Выводим тег
    print(f"{prefix}📁 {data['tag']}")
    
    # Выводим атрибуты
    if data['attributes']:
        print(f"{prefix}  📋 Атрибуты:")
        for key, value in data['attributes'].items():
            print(f"{prefix}    • {key} = {value}")
    
    # Выводим текстовое содержимое
    if data['text']:
        print(f"{prefix}  💬 Текст: {data['text']}")
    
    # Рекурсивно выводим детей
    if data['children']:
        for child in data['children']:
            print_xml_structure(child, indent + 2, max_depth)


def extract_all_values_flat(data: Dict[str, Any], path: str = "", results: List[tuple] = None) -> List[tuple]:
    """
    Извлечение всех значений тегов и атрибутов в плоский список.
    
    Args:
        data: Словарь с данными от parse_element
        path: Текущий путь в XML (XPath-подобный)
        results: Список для накопления результатов
        
    Returns:
        Список кортежей (путь, тип, имя, значение)
    """
    if results is None:
        results = []
    
    current_path = f"{path}/{data['tag']}" if path else data['tag']
    
    # Добавляем информацию о самом теге
    results.append((
        current_path,
        'tag',
        data['tag'],
        data['text'] if data['text'] else ''
    ))
    
    # Добавляем все атрибуты
    for attr_name, attr_value in data['attributes'].items():
        results.append((
            current_path,
            'attribute',
            attr_name,
            attr_value
        ))
    
    # Рекурсивно обрабатываем детей
    for child in data['children']:
        extract_all_values_flat(child, current_path, results)
    
    return results


def print_all_values_table(values: List[tuple]):
    """
    Вывод всех значений в виде таблицы.
    
    Args:
        values: Список кортежей от extract_all_values_flat
    """
    print("\n" + "=" * 120)
    print("ПОЛНЫЙ СПИСОК ВСЕХ ТЕГОВ И АТРИБУТОВ")
    print("=" * 120)
    print(f"{'№':<4} {'Путь':<50} {'Тип':<12} {'Имя':<25} {'Значение'}")
    print("-" * 120)
    
    for idx, (path, item_type, name, value) in enumerate(values, 1):
        # Ограничиваем длину вывода для читаемости
        path_display = path[:47] + "..." if len(path) > 50 else path
        value_display = str(value)[:70] + "..." if len(str(value)) > 70 else value
        
        print(f"{idx:<4} {path_display:<50} {item_type:<12} {name:<25} {value_display}")
    
    print("=" * 120)
    print(f"Всего элементов: {len(values)}")
    print("=" * 120)


def parse_egrul_structured(xml_file_path: str) -> Dict[str, Any]:
    """
    Структурированный парсинг выписки ЕГРЮЛ с выделением ключевых данных.
    
    Это специализированная функция для извлечения основных реквизитов организации.
    
    Args:
        xml_file_path: Путь к XML файлу
        
    Returns:
        Словарь с основными реквизитами организации
    """
    tree = ET.parse(xml_file_path)
    root = tree.getroot()
    
    # Ищем элемент СвЮЛ (основная информация о юрлице)
    sv_yul = root.find('.//СвЮЛ')
    
    if sv_yul is None:
        return {}
    
    # Базовые атрибуты юрлица
    result = {
        'огрн': sv_yul.get('ОГРН'),
        'инн': sv_yul.get('ИНН'),
        'кпп': sv_yul.get('КПП'),
        'дата_выдачи': sv_yul.get('ДатаВып'),
        'дата_огрн': sv_yul.get('ДатаОГРН'),
        'код_опф': sv_yul.get('КодОПФ'),
        'полное_наименование_опф': sv_yul.get('ПолнНаимОПФ')
    }
    
    # Полное наименование организации
    sv_nam_yul = sv_yul.find('.//СвНаимЮЛ')
    if sv_nam_yul is not None:
        result['полное_наименование'] = sv_nam_yul.get('НаимЮЛПолн')
    
    # Сокращённое наименование
    sv_nam_sokr = sv_yul.find('.//СвНаимЮЛСокр')
    if sv_nam_sokr is not None:
        result['сокращённое_наименование'] = sv_nam_sokr.get('НаимСокр')
    
    # Адрес (по ФИАС)
    sv_addr_fias = sv_yul.find('.//СвАдрЮЛФИАС')
    if sv_addr_fias is not None:
        result['адрес'] = {
            'индекс': sv_addr_fias.get('Индекс'),
            'регион': sv_addr_fias.findtext('.//Регион'),
            'наименование_региона': sv_addr_fias.findtext('.//НаимРегион'),
            'улица': None,
            'дом': None,
            'корпус': None,
            'помещение': None
        }
        
        # Извлекаем элементы адреса
        ulica = sv_addr_fias.find('.//ЭлУлДорСети')
        if ulica is not None:
            result['адрес']['улица'] = f"{ulica.get('Тип')} {ulica.get('Наим')}"
        
        zdanie = sv_addr_fias.find('.//Здание[@Тип="Д."]')
        if zdanie is not None:
            result['адрес']['дом'] = zdanie.get('Номер')
        
        korpus = sv_addr_fias.find('.//Здание[@Тип="К."]')
        if korpus is not None:
            result['адрес']['корпус'] = korpus.get('Номер')
        
        pomesh = sv_addr_fias.find('.//ПомещЗдания')
        if pomesh is not None:
            result['адрес']['помещение'] = f"{pomesh.get('Тип')} {pomesh.get('Номер')}"
    
    # Уставный капитал
    sv_ustkap = sv_yul.find('.//СвУстКап')
    if sv_ustkap is not None:
        result['уставный_капитал'] = {
            'вид': sv_ustkap.get('НаимВидКап'),
            'сумма': sv_ustkap.get('СумКап')
        }
    
    # Руководитель
    sv_dolzhn = sv_yul.find('.//СведДолжнФЛ')
    if sv_dolzhn is not None:
        sv_fl = sv_dolzhn.find('.//СвФЛ')
        sv_dol = sv_dolzhn.find('.//СвДолжн')
        
        result['руководитель'] = {}
        if sv_fl is not None:
            result['руководитель']['фамилия'] = sv_fl.get('Фамилия')
            result['руководитель']['имя'] = sv_fl.get('Имя')
            result['руководитель']['отчество'] = sv_fl.get('Отчество')
            result['руководитель']['инн'] = sv_fl.get('ИННФЛ')
        
        if sv_dol is not None:
            result['руководитель']['должность'] = sv_dol.get('НаимДолжн')
    
    # Учредители
    founders = []
    for uchr in sv_yul.findall('.//УчрФЛ'):
        sv_fl = uchr.find('.//СвФЛ')
        dolya = uchr.find('.//ДоляУстКап')
        
        if sv_fl is not None:
            founder = {
                'фамилия': sv_fl.get('Фамилия'),
                'имя': sv_fl.get('Имя'),
                'отчество': sv_fl.get('Отчество'),
                'инн': sv_fl.get('ИННФЛ')
            }
            
            if dolya is not None:
                percent = dolya.findtext('.//Процент')
                founder['доля_процент'] = percent
                founder['номинальная_стоимость'] = dolya.get('НоминСтоим')
            
            founders.append(founder)
    
    if founders:
        result['учредители'] = founders
    
    # Основной ОКВЭД
    sv_okved_osn = sv_yul.find('.//СвОКВЭДОсн')
    if sv_okved_osn is not None:
        result['основной_оквэд'] = {
            'код': sv_okved_osn.get('КодОКВЭД'),
            'наименование': sv_okved_osn.get('НаимОКВЭД')
        }
    
    # Дополнительные ОКВЭД
    additional_okved = []
    for sv_okved_dop in sv_yul.findall('.//СвОКВЭДДоп'):
        additional_okved.append({
            'код': sv_okved_dop.get('КодОКВЭД'),
            'наименование': sv_okved_dop.get('НаимОКВЭД'),
            'версия': sv_okved_dop.get('ПрВерсОКВЭД')
        })
    
    if additional_okved:
        result['дополнительные_оквэд'] = additional_okved
    
    return result


def main():
    """Основная функция для демонстрации всех методов парсинга."""
    
    xml_file_path = "pri_1.xml"
    
    print("=" * 80)
    print("XML ПАРСЕР ВЫПИСКИ ЕГРЮЛ")
    print("=" * 80)
    
    # ========== 1. Полный рекурсивный парсинг ==========
    print("\n🔍 1. ПОЛНЫЙ РЕКУРСИВНЫЙ ПАРСИНГ")
    print("-" * 80)
    
    try:
        full_data = parse_xml_full(xml_file_path)
        print("✅ XML успешно распарсен")
        print(f"📊 Корневой тег: {full_data['tag']}")
        print(f"📊 Количество дочерних элементов: {len(full_data['children'])}")
        
        # Выводим структуру (первые 3 уровня глубины)
        print("\n📋 СТРУКТУРА XML (первые 3 уровня):")
        print_xml_structure(full_data, max_depth=3)
        
    except FileNotFoundError:
        print(f"❌ Файл {xml_file_path} не найден!")
        return
    except ET.ParseError as e:
        print(f"❌ Ошибка парсинга XML: {e}")
        return
    
    # ========== 2. Плоский список всех значений ==========
    print("\n\n🔍 2. ПЛОСКИЙ СПИСОК ВСЕХ ТЕГОВ И АТРИБУТОВ")
    print("-" * 80)
    
    all_values = extract_all_values_flat(full_data)
    print_all_values_table(all_values)
    
    # ========== 3. Структурированный вывод по реквизитам ==========
    print("\n\n🔍 3. СТРУКТУРИРОВАННЫЕ ДАННЫЕ ОРГАНИЗАЦИИ")
    print("-" * 80)
    
    structured_data = parse_egrul_structured(xml_file_path)
    
    if structured_data:
        print("\n🏢 ОСНОВНЫЕ РЕКВИЗИТЫ:")
        print(f"   ОГРН: {structured_data.get('огрн')}")
        print(f"   ИНН: {structured_data.get('инн')}")
        print(f"   КПП: {structured_data.get('кпп')}")
        print(f"   Дата выдачи: {structured_data.get('дата_выдачи')}")
        print(f"   Полное наименование: {structured_data.get('полное_наименование')}")
        print(f"   Сокращённое наименование: {structured_data.get('сокращённое_наименование')}")
        
        if 'адрес' in structured_data and structured_data['адрес']:
            print(f"\n📍 АДРЕС:")
            addr = structured_data['адрес']
            print(f"   Индекс: {addr.get('индекс')}")
            print(f"   Регион: {addr.get('наименование_региона')}")
            print(f"   Улица: {addr.get('улица')}")
            print(f"   Дом: {addr.get('дом')}")
            if addr.get('корпус'):
                print(f"   Корпус: {addr.get('корпус')}")
            if addr.get('помещение'):
                print(f"   Помещение: {addr.get('помещение')}")
        
        if 'уставный_капитал' in structured_data:
            print(f"\n💰 УСТАВНЫЙ КАПИТАЛ:")
            uk = structured_data['уставный_капитал']
            print(f"   Вид: {uk.get('вид')}")
            print(f"   Сумма: {uk.get('сумма')} руб.")
        
        if 'руководитель' in structured_data:
            print(f"\n👤 РУКОВОДИТЕЛЬ:")
            director = structured_data['руководитель']
            print(f"   ФИО: {director.get('фамилия')} {director.get('имя')} {director.get('отчество')}")
            print(f"   Должность: {director.get('должность')}")
            print(f"   ИНН: {director.get('инн')}")
        
        if 'учредители' in structured_data:
            print(f"\n👥 УЧРЕДИТЕЛИ:")
            for idx, founder in enumerate(structured_data['учредители'], 1):
                print(f"   {idx}. {founder.get('фамилия')} {founder.get('имя')} {founder.get('отчество')}")
                print(f"      ИНН: {founder.get('инн')}")
                print(f"      Доля: {founder.get('доля_процент')}%")
                print(f"      Номинальная стоимость: {founder.get('номинальная_стоимость')} руб.")
        
        if 'основной_оквэд' in structured_data:
            print(f"\n🎯 ОСНОВНОЙ ОКВЭД:")
            okved = structured_data['основной_оквэд']
            print(f"   Код: {okved.get('код')}")
            print(f"   Наименование: {okved.get('наименование')}")
        
        if 'дополнительные_оквэд' in structured_data:
            print(f"\n📋 ДОПОЛНИТЕЛЬНЫЕ ОКВЭД (всего: {len(structured_data['дополнительные_оквэд'])}):")
            for idx, okved in enumerate(structured_data['дополнительные_оквэд'][:10], 1):
                print(f"   {idx}. {okved.get('код')} - {okved.get('наименование')[:60]}...")
            if len(structured_data['дополнительные_оквэд']) > 10:
                print(f"   ... и ещё {len(structured_data['дополнительные_оквэд']) - 10} записей")
    
    # ========== 4. Сохранение результатов в файл ==========
    print("\n\n🔍 4. СОХРАНЕНИЕ РЕЗУЛЬТАТОВ В ФАЙЛ")
    print("-" * 80)
    
    # Сохраняем плоский список в CSV
    import csv
    with open('egrul_parsed_all_values.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['№', 'Путь', 'Тип', 'Имя', 'Значение'])
        for idx, (path, item_type, name, value) in enumerate(all_values, 1):
            writer.writerow([idx, path, item_type, name, value])
    
    print("✅ Сохранено в файл: egrul_parsed_all_values.csv")
    
    # Сохраняем структурированные данные в JSON
    import json
    with open('egrul_structured_data.json', 'w', encoding='utf-8') as f:
        json.dump(structured_data, f, ensure_ascii=False, indent=2)
    
    print("✅ Сохранено в файл: egrul_structured_data.json")
    
    print("\n" + "=" * 80)
    print("ПАРСИНГ ЗАВЕРШЁН УСПЕШНО!")
    print("=" * 80)


if __name__ == "__main__":
    main()
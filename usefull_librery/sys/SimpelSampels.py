'''
Разбираем модуль sys

Модуль sys предоставляет системе особые параметры и функции. В данном разделе мы рассмотрим следующее:

sys.argv
sys.executable
sys.exit
sys.modules
sys.path
sys.platform
sys.stdin/stdout/stderr
    
Athor: Gansior Alexander, gansior@gansior.ru, +79173383804
Starting 2022//
Ending 2022//
    
'''

import sys
    
from termcolor import cprint
import inspect

'''
Text colors: grey red green yellow blue magenta cyan white
Text highlights: on_grey on_red on_green on_yellow on_blue on_magenta on_cyan on_white
Attributes: bold dark underline blink reverse concealed
template --> cprint(f'{}' , 'red', attrs=['bold'])

Shows which module is currently running
cprint("="*20 + " >> " + inspect.stack()[0][0].f_code.co_name + " << "+"="*20, 'red', attrs=['bold'])
'''
    
    
def sys_argv():
    """
    Значение sys.argv – это список аргументов командной строки, которые причастны к скрипту Python. 
    Первый аргумент, argv[0], имеет аналогичное скрипту Python наименование. В зависимости от платформы, 
    на которой вы работаете, первый аргумент может содержать полный путь к скрипту или к названию файла. 
    Для дополнительных деталей обратитесь к документации.
    А тем временем, попробуем поработать с парочкой примеров, чтобы познакомиться с этим инструментом:
    Keyword arguments:
    argument -- description
    Return: return_description
    """
    print()
    cprint("="*20 + " >> " + inspect.stack()[0][0].f_code.co_name + " << "+"="*20, 'red', attrs=['bold'])
    cprint(f'{sys.argv}' , 'red', attrs=['bold'])
    
    
def sys_executable():
    """Значение sys.executable – это полный путь к интерпретатору Python. 
    Это очень полезно, когда вы используете чей-то компьютер, и вам нужно узнать, где установлен Python. 
    В некоторых системах, данная команда не сработает, и выдаст пустую строку с надписью None. 

    """
    print()
    cprint("="*20 + " >> " + inspect.stack()[0][0].f_code.co_name + " << "+"="*20, 'red', attrs=['bold'])
    cprint(f'{sys.executable}' , 'red', attrs=['bold'])
    

def sys_path():
    """
        Значение функции path модуля sys – это список строк, которые указывают путь поиска для модулей. 
        Как правило, данная функция указывает Python, в каких локациях смотреть, когда он пытается импортировать модуль. 
        В соответствии с документацией Python, sys.path инициализируется из переменной окружения PYTHONPATH, плюс зависимое от 
        установки значение, указанное по умолчанию. 

    """
    print()
    cprint("="*20 + " >> " + inspect.stack()[0][0].f_code.co_name + " << "+"="*20, 'red', attrs=['bold'])
    for k in sys.path:
        cprint(f'{k}' , 'green', attrs=['bold'])

    
    
if __name__ == '__main__':
    name=''
    sys_argv()
    sys_executable()
    sys_path()
    print()
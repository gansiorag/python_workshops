'''
This module make

Athor: Gansior Alexander, gansior@gansior.ru, +79173383804
Starting 2022//
Ending 2022//

'''

import os
import sys
import inspect
from termcolor import cprint

# Text colors: grey red green yellow blue magenta cyan white
# Text highlights: on_grey on_red on_green on_yellow on_blue on_magenta on_cyan on_white
# Attributes: bold dark underline blink reverse concealed
# template --> cprint(f'{}' , 'red', attrs=['bold'])

# Shows which module is currently running
# cprint('='*20 + ' >> ' + inspect.stack()[0][0].f_code.co_name +
# ' << '+'='*20, 'red', attrs=['bold'])


NAME_PROJECT = 'python_workshops'
cprint(os.getcwd(), 'green')
path_prj = os.getcwd().split(NAME_PROJECT)[0] + NAME_PROJECT + '/'
cprint(path_prj, 'blue')
sys.path.append(path_prj)

from fun1 import print_hello
from fun2 import print_no


def prog1():
    '''AI is creating summary for prog1
    '''
    cprint('='*20 + ' >> ' + inspect.stack()[0][0].f_code.co_name +
           ' << '+'='*20, 'red', attrs=['bold'])
    print_hello()

def prog2():
    '''AI is creating summary for prog2
    '''
    cprint('='*20 + ' >> ' + inspect.stack()[0][0].f_code.co_name +
           ' << '+'='*20, 'red', attrs=['bold'])
    print_no()

if __name__ == '__main__':
    NAME = ''
    prog1()
    prog2()

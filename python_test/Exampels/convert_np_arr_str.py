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
import numpy as np

# Text colors: grey red green yellow blue magenta cyan white
# Text highlights: on_grey on_red on_green on_yellow on_blue on_magenta on_cyan on_white
# Attributes: bold dark underline blink reverse concealed
# template --> cprint(f'{}' , 'red', attrs=['bold'])

# Shows which module is currently running
# cprint('='*20 + ' >> ' + inspect.stack()[0][0].f_code.co_name +
# ' << '+'='*20, 'red', attrs=['bold'])


NAME_PROJECT = '****** Your project name '
cprint(os.getcwd(), 'green')
path_prj = os.getcwd().split(NAME_PROJECT)[0] + NAME_PROJECT + '/'
cprint(path_prj, 'blue')
sys.path.append(path_prj)


def prog1():
    '''AI is creating summary for prog1
    '''
    print()
    cprint('='*20 + ' >> ' + inspect.stack()[0][0].f_code.co_name +
           ' << '+'='*20, 'red', attrs=['bold'])
    print()

    state_codes = np.array([1, 2, 4, 5, 6])
    list_of_strings = state_codes.astype(str).tolist()
    print(list_of_strings)
    print(all(isinstance(item, str) for item in list_of_strings))


def prog2():
    '''AI is creating summary for prog2
    '''
    print()
    cprint('='*20 + ' >> ' + inspect.stack()[0][0].f_code.co_name +
           ' << '+'='*20, 'red', attrs=['bold'])
    print()

    area_codes = np.array([212, 213, 312, 415, 305])
    list_of_strings = list(map(str, area_codes))
    print(list_of_strings)
    print(all(isinstance(item, str) for item in list_of_strings))
    print()
    tt = ['1', '2', '']
    print(all(tt))
    print()


if __name__ == '__main__':
    NAME = ''
    prog1()
    prog2()

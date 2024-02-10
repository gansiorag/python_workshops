'''
This module work with diferent formats of date and convert to integer/

Athor: Gansior Alexander, gansior@gansior.ru, +79173383804
Starting 2024/02/10
Ending v1/ 2024/02/10

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


def hour_str_to_int(serv_list: str):
    """ Convert time hour, minute, secundes in 
    integer
    Format of time can be different - 101010, 10/10/10, 10.10.10, 10:10-10 and
e.t.

    Args:
        serv_list (str): ['time in str] .

    Returns:
        [type]: [int]
    """
    print()
    cprint('='*20 + ' >> ' + inspect.stack()[0][0].f_code.co_name +
           ' << '+'='*20, 'red', attrs=['bold'])
    print()

    if len(serv_list) == 6:
        hour = serv_list[0:2]
        minut = serv_list[2:4]
        sek = serv_list[4:6]
    if len(serv_list) == 8:
        hour = serv_list[0:2]
        minut = serv_list[3:5]
        sek = serv_list[6:8]
    hour_int = int(hour) * 60 * 60
    minut_int = int(minut) * 60
    sek_int = int(sek)
    total = hour_int + minut_int + sek_int
    return total


def prog2():
    '''AI is creating summary for prog2
    '''
    print()
    cprint('='*20 + ' >> ' + inspect.stack()[0][0].f_code.co_name +
           ' << '+'='*20, 'red', attrs=['bold'])
    print()


# part of demo and test
if __name__ == '__main__':

    # test hour_str_to_int(serv_list: str)
    d1 = hour_str_to_int('201010')
    print(d1)
    d1 = hour_str_to_int('20-10-10')
    print(d1)
    d1 = hour_str_to_int('20.10.10')
    print(d1)
    d1 = hour_str_to_int('20:10:10')
    print(d1)
    d1 = hour_str_to_int('20:10-10')
    print(d1)

    prog2()

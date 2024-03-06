'''
This module work with diferent formats of date and convert to integer/

Athor: Gansior Alexander, gansior@gansior.ru, +79173383804
Starting 2024/02/10
Ending v1/ 2024/02/10

'''

import os
import sys
from datetime import datetime as dt
from datetime import timedelta, datetime
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


def get_year_month_day_from_str(date_str: str):
    """ Convert time hour, minute, secundes in
    integer
    Format of time can be different - 20221201, 2022/10/10, 2022.10.10,
    2022:10-10, 01122022, 10/10/2022, 10.10.2022, 10-10:2022
e.t.

    Args:
        date_str (str): ['time in str] .

    Returns:
        [type]: [int]
        year, month, day
    """
    print()
    cprint('='*20 + ' >> ' + inspect.stack()[0][0].f_code.co_name +
           ' << '+'='*20, 'red', attrs=['bold'])
    print()
    year = 0
    month = 0
    day = 0
    print(date_str)
    if len(date_str) == 8:
        year = int(date_str[0:4])
        month = int(date_str[4:6])
        day = int(date_str[6:8])
    if len(date_str) == 10:
        date_str = date_str.replace(':', ' ').replace('/', ' ')
        date_str = date_str.replace('.', ' ').replace('-', ' ')
        print(date_str)
        date_str_l = date_str.split()
        if len(date_str_l[0]) == 4:
            year = int(date_str_l[0])
            month = int(date_str_l[1])
            day = int(date_str_l[2])
        else:
            year = int(date_str_l[2])
            month = int(date_str_l[1])
            day = int(date_str_l[0])
    return year, month, day


def get_date_with_step(date_start: str, step_sek: int, date_gard: str):
    """_summary_

    Args:
        date_start (str): _description_
        step_sek (int): _description_
        date_gard (str): _description_
    """

    date_start_d = dt.strptime(date_start, '%Y-%m-%d %H:%M:%S')
    date_gard_d = dt.strptime(date_gard, '%Y-%m-%d %H:%M:%S')
    time_del = timedelta(seconds=step_sek)
    ss = 0
    print(date_start_d)
    while date_gard_d > date_start_d:
        date_start_d = date_start_d + time_del
        ss += 1
    print(date_start_d)
    print(date_gard_d)
    print(ss)


# part of demo and test
if __name__ == '__main__':

    print(get_year_month_day_from_str('2011010'))
    print()
    print(get_year_month_day_from_str('2011-10-10'))
    print()
    print(get_year_month_day_from_str('10-10-2011'))
    print()
    print(get_year_month_day_from_str('2010:10-10'))
    print()
    print(get_year_month_day_from_str('2011/01/20'))
    print()
    get_date_with_step('2024-02-18 01:21:09', 12, '2024-03-01 00:00:00')

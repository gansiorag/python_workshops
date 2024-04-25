'''
 This module make

Athor: Gansior Alexander, gansior@gansior.ru, +79173383804
Starting 2022//
Ending 2022//

https://github.com/python-lz4/python-lz4/blob/master/docs/quickstart.rst

pip install lz4
'''

import os
import sys
import inspect
from termcolor import cprint
import lz4.frame

# Text colors: grey red green yellow blue magenta cyan white
# Text highlights: on_grey on_red on_green on_yellow on_blue on_magenta on_cyan on_white
# Attributes: bold dark underline blink reverse concealed
# template --> cprint(f'{}' , 'red', attrs=['bold'])


NAME_PROJECT = '******'
cprint(os.getcwd(), 'green')
PATH_PRJ = os.getcwd().split(NAME_PROJECT)[0] + NAME_PROJECT + '/'
cprint(PATH_PRJ, 'blue')
sys.path.append(PATH_PRJ)


def prog_unzip(n_f: str):
    cprint('='*20 + ' >> ' + inspect.stack()[0][0].f_code.co_name + ' << '+'='*20, 'red', attrs=['bold'])
    # with open(n_f, 'rb') as i_f:
    #     dd = i_f.read()
    i_dd = 'kljlk sedflkjlk nkjhkj ewrwe fwsfs'.encode()
    compressed = lz4.frame.compress(i_dd)
    decompressed = lz4.frame.decompress(compressed).decode()
    print(decompressed)


def prog2():
    cprint('='*20 + ' >> ' + inspect.stack()[0][0].f_code.co_name + ' << '+'='*20, 'red', attrs=['bold'])


if __name__ == '__main__':
    NAME = '/home/gansiorag/MyParth/ProjectMy/my_learn_docker/proba_feache/work_lz4.py'
    prog_unzip(NAME)
    prog2()
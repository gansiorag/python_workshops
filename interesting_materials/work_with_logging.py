'''
Sourse: https://pythononline.ru/osnovy/python-stdin-stdout-stderr

This module make

Athor: Gansior Alexander, gansior@gansior.ru, +79173383804
Starting 2024//
Ending 2024//

'''

import os
import sys
import inspect
from termcolor import cprint

# Text colors: grey red green yellow blue magenta cyan white
# Text highlights: on_grey on_red on_green on_yellow on_blue on_magenta on_cyan on_white
# Attributes: bold dark underline blink reverse concealed
# template --> cprint(f'{}' , 'red', attrs=['bold'])


NAME_PROJECT = 'python_workshops'
cprint(os.getcwd(), 'green')
PATH_PRJ = os.getcwd().split(NAME_PROJECT)[0] + NAME_PROJECT + '/'
cprint(PATH_PRJ, 'blue')
sys.path.append(PATH_PRJ)


def use_stdout():
    cprint('='*20 + ' >> START ' + inspect.stack()
           [0][0].f_code.co_name + ' << '+'='*20, 'red', attrs=['bold'])
    print()
    stdout_fileno = sys.stdout
    sample_input = ['Hi', 'Hello from AskPython', 'exit']
    for ip in sample_input:
        # Prints to stdout
        stdout_fileno.write(ip + '\n' + '!!!!')
    print()
    cprint('='*20 + ' >> END ' + inspect.stack()
           [0][0].f_code.co_name + ' << '+'='*20, 'red', attrs=['bold'])


def use_stderr():
    print()
    cprint('='*20 + ' >> START ' + inspect.stack()
           [0][0].f_code.co_name + ' << '+'='*20, 'red', attrs=['bold'])
    stdout_fileno = sys.stdout
    stderr_fileno = sys.stderr
    sample_input = ['Hi', 'Hello from AskPython', 'exit']
    for ip in sample_input:
        # Prints to stdout
        stdout_fileno.write(ip + '\n')
        # Tries to add an Integer with string. Raises an exception
        try:
            ip = ip + 100
            # Catch all exceptions
        except Exception as err:
            stderr_fileno.write('Exception Occurred!\n')
            stderr_fileno.write(err)
    print()
    cprint('='*20 + ' >> END ' + inspect.stack()
           [0][0].f_code.co_name + ' << '+'='*20, 'red', attrs=['bold'])


if __name__ == '__main__':
    NAME = ''
    use_stdout()
    use_stderr()

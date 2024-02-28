'''
This module make

Athor: Gansior Alexander, gansior@gansior.ru, +79173383804
Starting 2022//
Ending 2022//

'''

import os
import sys
import aiohttp
import asyncio
import inspect
from termcolor import cprint

# Text colors: grey red green yellow blue magenta cyan white
# Text highlights: on_grey on_red on_green on_yellow on_blue on_magenta
# on_cyan on_white
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
    resp = asyncio.request(method, url, body=None, headers={})

def prog2():
    '''AI is creating summary for prog2
    '''
    print()
    cprint('='*20 + ' >> ' + inspect.stack()[0][0].f_code.co_name +
           ' << '+'='*20, 'red', attrs=['bold'])
    print()


async def send_request():
    async with aiohttp.ClientSession() as session:
        url = 'https://google.com'
        async with session.get(url) as response:
            print('responce   ')
            data = await response.text()
            print(data)


if __name__ == '__main__':
    NAME = ''
    loop = asyncio.get_event_loop()
    loop.run_until_complete(send_request())
    prog1()
    prog2()

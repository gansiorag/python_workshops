'''
This module make

Athor: Gansior Alexander, gansior@gansior.ru, +79173383804
Starting 2024/01/06
Ending 2024//
pip install pytube
'''

import os
import sys
import inspect
from termcolor import cprint
from pytube import YouTube

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


def download_video(video_url, save_path):
    '''AI is creating summary for prog1
    '''
    print()
    cprint('='*20 + ' >> ' + inspect.stack()[0][0].f_code.co_name +
           ' << '+'='*20, 'red', attrs=['bold'])
    print()
    try:
        yt = YouTube(video_url)
        video_stream = yt.streams.get_highest_resolution()
        video_stream.download(output_path=save_path)
        print('download completiv !!!')
    except Exception as e:
        print("Error: ", str(e))


def start_load():
    '''AI is creating summary for prog2
    '''
    print()
    cprint('='*20 + ' >> ' + inspect.stack()[0][0].f_code.co_name +
           ' << '+'='*20, 'red', attrs=['bold'])
    print()

    video_link = "https://www.youtube.com/watch?v=TumfGqUf39U&list=PLD5U-C5KK50XMCBkY0U-NLzglcRHzOwAg&index=12"
    save_path = "/home/al/Projects_My/python_workshops/interesting_libraries/feaches/rezult_yotube/"
    download_video(video_link, save_path)


if __name__ == '__main__':
    NAME = ''
    start_load()

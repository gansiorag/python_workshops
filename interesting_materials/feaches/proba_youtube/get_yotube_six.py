"""
This module make

Athor: Gansior Alexander, gansior@gansior.ru, +79173383804
Starting 2024/01/06
Ending 2024//
pip install pytube
"""

import os
import sys
import inspect
from termcolor import cprint
import os.path
import time
import requests
from tqdm import tqdm
import json

# Text colors: grey red green yellow blue magenta cyan white
# Text highlights: on_grey on_red on_green on_yellow on_blue on_magenta on_cyan on_white
# Attributes: bold dark underline blink reverse concealed
# template --> cprint(f'{}' , 'red', attrs=['bold'])

# Shows which module is currently running
# cprint('='*20 + ' >> ' + inspect.stack()[0][0].f_code.co_name +
# ' << '+'='*20, 'red', attrs=['bold'])


NAME_PROJECT = "proba_youtube"
cprint(os.getcwd(), "green")
path_prj = os.getcwd().split(NAME_PROJECT)[0] + NAME_PROJECT + "/"
cprint(path_prj, "blue")
sys.path.append(path_prj)

import os
import subprocess

from pytube import YouTube
url = 'https://www.youtube.com/watch?v=wNRjR6Cds5s&list=PL2IsFZBGM_IHCl9zhRVC1EXTomkEp_1zm'
yt_video = YouTube(url)
videos = yt_video.streams.all()

# we are using enumerate to get the index number
res_list = list(enumerate(videos))
for i in res_list:
    print(i)

resolution = int(input("Enter the index number of the video : "))
videos[resolution].download()
print('your video is downloaded successfully')

# if __name__ == "__main__":
#     video_url = "https://www.youtube.com/watch?v=wNRjR6Cds5s&list=PL2IsFZBGM_IHCl9zhRVC1EXTomkEp_1zm"  # Example video URL
#     download_video(video_url)

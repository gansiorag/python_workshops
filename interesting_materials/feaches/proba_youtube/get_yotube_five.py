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

def download_video(video_url):
    command = [
        'yt-dlp',  # or 'yt-dlp' if you installed yt-dlp
        '-o', './%(title)s.%(ext)s',  # Output template
        video_url
    ]
    
    try:
        subprocess.run(command, check=True)
        print("Download completed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    video_url = "https://www.youtube.com/watch?v=wNRjR6Cds5s&list=PL2IsFZBGM_IHCl9zhRVC1EXTomkEp_1zm"  # Example video URL
    download_video(video_url)

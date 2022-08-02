'''
 This module collected different usefull libraries 
    
Athor: Gansior Alexander, gansior@gansior.ru, +79173383804
Starting 2022//
Ending 2022//
    
'''
    
"""
1.) Convert Images to PDF
If you had a lot of images and looking for converting them into a single 
Pdf then this automation script will be handy for you.
Method 1-

"""
import os
import img2pdf
with open("out.pdf", "wb") as file:
   file.write(img2pdf.convert([i for i in os.listdir('Path of image_Directory') if i.endswith(".jpg")]))
    
# Method 2 -

from fpdf import FPDF
Pdf = FPDF()
list_of_images = ["one.jpg", "second.jpg","third.jpg"]
for i in list_of_images:
   Pdf.add_page()
   Pdf.image(i,x,y,w,h)
   Pdf.output("out.pdf", "F")
   
"""
2.) Convert PDF to CSV
Sometimes we need to convert our PDF data into CSV format, 
So for that kind of work, this Python script will be handy for you.
"""
import tabula
filename = input("Enter File Path: ")
df = tabula.read_pdf(filename, encoding='utf-8', spreadsheet=True, pages='1')
df.to_csv('out.csv')


"""
    3.) YT Video Downloader
A simple automation script to download Youtube videos. 
No need of any websites or apps, just use the below code to download any video.
"""

import pytube
link = input('Enter The Youtube Video URL')
dn = pytube.Youtube(link)
dn.streams.first().download()
print('Your Video Has Been Downloaded', link)

"""
    4.) InstaDpViewer
This script will download the DP of any Instagram User. 
It uses module instaloader which takes username as input and 
downloads the DP as an output.
"""
import instaloader
il = instaloader.Instaloader()
username = input("Enter Insta username ")
il.download_profile(username , profile_pic_only=True)
print("Your DP is Downloaded")

"""
    5.) Text to Speech
It uses google Text to Speech API to convert your 
written Text to AI bot voice.

    """
from pygame import mixer
from gtts import gTTS

tts = gTTS('Like This Article')
tts.save('output.mp3')
mixer.init()
mixer.music.load('output.mp3')
mixer.music.play()


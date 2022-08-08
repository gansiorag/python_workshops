'''
 This module make 

pip install -c conda-forge poppler    
Athor: Gansior Alexander, gansior@gansior.ru, +79173383804
Starting 2022//
Ending 2022//
    
'''
    
from termcolor import cprint
'''
Text colors: grey red green yellow blue magenta cyan white
Text highlights: on_grey on_red on_green on_yellow on_blue on_magenta on_cyan on_white
Attributes: bold dark underline blink reverse concealed
'''

from pdf2image import convert_from_path
from pdf2image import convert_from_bytes

    
def prog1():


    # incase of Linux we don't have to provide the popper_path parameter
    images = convert_from_path(
        'my_pdf_file.pdf', poppler_path=r"poppler-0.68.0_x86\poppler-0.68.0\bin")

    for i in range(len(images)):
        # Save pages as images in the pdf
        images[i].save(f'image_{i+1}.png', 'PNG')
    
    
def prog2():
    images = convert_from_bytes(open('my_pdf_file.pdf', 'rb').read(
    ), poppler_path=r"poppler-0.68.0_x86\poppler-0.68.0\bin")
    for i in range(len(images)):
        # Save pages as images in the pdf
        images[i].save(f'image_{i+1}.png', 'PNG')
    
    
if __name__ == '__main__':
    name=''
    prog1()
    prog2()
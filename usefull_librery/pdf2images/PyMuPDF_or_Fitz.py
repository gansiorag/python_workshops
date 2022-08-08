'''
 This module make 

pip install PyMuPDF==1.16.14
 
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
 
import fitz   
    
def prog1():
    pdffile = "my_pdf_file.pdf"
    doc = fitz.open(pdffile)

    try:
        for i in range(100):
            page = doc.load_page(i)
            pix = page.get_pixmap()
            pix.save(f"image_{i+1}.png")
    except:
        print(f"Number of pages {i}")
    
    
def prog2():
    pass
    
    
if __name__ == '__main__':
    name=''
    prog1()
    prog2()
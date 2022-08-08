'''
 This module make 
    
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


from pdf2jpg import pdf2jpg
    
    
def prog1():
    inputpath = r"my_pdf_file.pdf"
    outputpath = r""
    result = pdf2jpg.convert_pdf2jpg(inputpath,outputpath, pages="ALL")
    
    
def prog2():
    pass
    
    
if __name__ == '__main__':
    name=''
    prog1()
    prog2()
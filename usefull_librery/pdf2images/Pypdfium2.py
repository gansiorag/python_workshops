'''
 This module make 
pip3 install –no-build-isolation -U pypdfium2
    
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
import pypdfium2 as pdfium    
    
def prog1():
    pdf = pdfium.PdfDocument("my_pdf_file.pdf")
    n_pages = len(pdf)
    for page_number in range(n_pages):
        page = pdf.get_page(page_number)
        pil_image = page.render_topil(
            scale=1,
            rotation=0,
            crop=(0, 0, 0, 0),
            colour=(255, 255, 255, 255),
            annotations=True,
            greyscale=False,
            optimise_mode=pdfium.OptimiseMode.NONE,
        )
        pil_image.save(f"image_{page_number+1}.png")
    
    
def prog2():
    pass
    
    
if __name__ == '__main__':
    name=''
    prog1()
    prog2()
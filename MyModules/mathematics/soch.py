'''
 This module make 
    
Athor: Gansior Alexander, gansior@gansior.ru, +79173383804
Starting 2022//
Ending 2022//
    
'''
    
from termcolor import cprint
import inspect
'''
Text colors: grey red green yellow blue magenta cyan white
Text highlights: on_grey on_red on_green on_yellow on_blue on_magenta on_cyan on_white
Attributes: bold dark underline blink reverse concealed
template --> cprint(f'{}' , 'red', attrs=['bold'])
    
    
Shows which module is currently running
cprint('='*20 + ' >> ' + inspect.stack()[0][0].f_code.co_name + ' << '+'='*20, 'red', attrs=['bold'])
'''
    
    
def prog1(comN, kN):
    l=1
    for k in range(1,comN) :
        l =l*k
    nn =1
    for k in range(1,kN) :
        nn =nn*k
    mm =1
    for k in range(1,comN - kN) :
        mm =mm*k
    
    return l/(nn*mm)
    
    
    
def prog2():
    pass
    
    
if __name__ == '__main__':
    name=''
    print(prog1(32,3)*prog1(32,3))
    #prog2()
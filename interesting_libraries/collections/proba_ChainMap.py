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
    
import os
import sys
 
nameProjectStart = 'python_workshops'
cprint(os.getcwd(), 'green')
PathPrj = os.getcwd().split(nameProjectStart)[0] + nameProjectStart +  '/'
cprint(PathPrj, 'blue')
sys.path.append(PathPrj)
    
from collections import ChainMap
    
def prog1():
    baseline = {'music': 'bach', 'art': 'rembrandt'}
    adjustments = {'art': 'van gogh', 'opera': 'carmen'}
    dd = list(ChainMap(adjustments, baseline))
    dd1 = list(ChainMap(adjustments))
    cprint(dd, 'red')
    cprint(dd1, 'green')
    
    
def prog2():
    pass
    
    
if __name__ == '__main__':
    name=''
    prog1()
    prog2()
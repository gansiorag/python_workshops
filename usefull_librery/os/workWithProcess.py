'''
 The functions presented below make it possible to manipulate the uid, 
 gid and pid process.
    
Athor: Gansior Alexander, gansior@gansior.ru, +79173383804
Starting 2022/08/12
Ending 2022//
    
'''
    
from termcolor import cprint
'''
Text colors: grey red green yellow blue magenta cyan white
Text highlights: on_grey on_red on_green on_yellow on_blue on_magenta on_cyan on_white
Attributes: bold dark underline blink reverse concealed
template --> cprint(f'{}' , 'red', attrs=['bold'])
'''
import os

TEST_GID = 1001
TEST_UID = 1001   
    
def show_user_info():
    cprint(f'Effective indicator groups process: {os.getegid()}', 'red', attrs=['bold'])
    cprint(f'id of User : {os.geteuid()}', 'red', attrs=['bold'])
    cprint(f'Group real idicator: {os.getgroups()}', 'blue', attrs=['bold'])
    cprint('indic Group of process pid:', os.getpgid(1000), 'green', attrs=['bold'])
    
    
def prog2():
    pass
    
    
if __name__ == '__main__':
    show_user_info()
    prog2()
'''
 This module make all fo linux/
    
Athor: Gansior Alexander, gansior@gansior.ru, +79173383804
Starting 2022/07/01
Ending 2022//
    
'''
    
from termcolor import cprint
'''
Text colors: grey red green yellow blue magenta cyan white
Text highlights: on_grey on_red on_green on_yellow on_blue on_magenta on_cyan on_white
Attributes: bold dark underline blink reverse concealed
'''

import subprocess

    
def example1():
    """_summary_
    linux call gedit
    """

    code = subprocess.call("gedit")
    if code == 0:
        cprint('='*20 + ' >> ' + "Success!" + ' << ' + '='*20, 'green')
    else:
        cprint('='*20 + ' >> ' + "Error!" + ' << ' + '='*20, 'red')
    
def example2():
    code = subprocess.call(["ping", "www.yahoo.com"])
    
    
def example3():
    """
    get data from ftp.zakupki.gov.ru
    user = free
    pass = free
    
    """
    
    # Constants
    FTP_HOST="ftp.zakupki.gov.ru"
    FTP_USER="free"
    FTP_PASS="free"
    FTP_FILE="/path.to/file.txt"
    FTP_DIR="/fcs_regions"
    
    command =["lftp", "-c",  f"open ftp://{FTP_USER}:{FTP_PASS}@ftp.zakupki.gov.ru; ls fcs_regions"] 
    print('print 1 ', command)
    #data = subprocess.call(command)
    data = subprocess.run(command, capture_output=True, encoding="utf-8").stdout.split('\n')
    for ll in data:
        if ll:
            print('print 2 ',ll.split()[-1])
    # try:
    #     subp = subprocess.Popen(command,
    #                             stdout=subprocess.PIPE)
    #                             # stderr=subprocess.PIPE,
    #                             # close_fds=True,
    #                             # bufsize=-1,
    #                             # universal_newlines=True)

    #     #data = subp.communicate()
    #     print(subp)
    # except FileNotFoundError as exception:
    #    print(f'Error {exception}')
    
    
if __name__ == '__main__':
    name=''
    #example1()
    #example2()
    example3()
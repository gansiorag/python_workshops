'''
 This module make: read dataset from link - ftp.zakupki.gov.ru
 use module subprocess. This module use commands of shell bash of linux/
    
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


class FTP():

    def __init__(self, proxy ='', ftpSource = '', userProxy = '',
                 passProxy = '', userSource = '', passSource = '') -> None:
        """_summary_

        Args:
            proxy (str, optional): _description_. Defaults to ''. 
            ftpSource (str, optional): _description_. Defaults to ''.
            userProxy (str, optional): _description_. Defaults to ''.
            passProxy (str, optional): _description_. Defaults to ''.
            userSource (str, optional): _description_. Defaults to ''.
            passSource (str, optional): _description_. Defaults to ''.
        """
        self.proxy = proxy
        self.ftpSource = ftpSource
        self.userProxy = userProxy
        self.passProxy = passProxy
        self.userSource = userSource 
        self.passSource = passSource

    def getDirectory(self, dirSource = ''):
        command =["lftp", "-c", f"open ftp://{self.userSource}:{self.passSource}@{self.ftpSource}; ls {dirSource}"] 
        print('print 1 ', command)
        #data = subprocess.call(command)
        data = subprocess.run(command, capture_output=True, encoding="utf-8").stdout.split('\n')
        #print(data)
        dirList = []
        for ll in data:
            if ll:
                dirList.append(ll.split()[-1])
        return dirList


    def getFile(self, fromFile = '', toFile = ''):
        command =["lftp", "-c", f"open ftp://{self.userSource}:{self.passSource}@{self.ftpSource};get {fromFile} -o {toFile}"] 
        print('print 1 ', command)
        #data = subprocess.call(command)
        data = subprocess.run(command, capture_output=True, encoding="utf-8")
        
    
    def getSizeFile(self, nameFile = '') -> int:
        """_summary_

        Args:
            nameFile (str, optional): _description_. Defaults to ''.

        Returns:
            int: _description_ - Return size file to kb
        """
        command =["lftp", "-c", f"open ftp://{self.userSource}:{self.passSource}@{self.ftpSource};cls -s {nameFile}"] 
        print('print 1 ', command)
        #data = subprocess.call(command)
        data = subprocess.run(command, capture_output=True, encoding="utf-8").stdout.split()   
        return int(data[0])

def test1():
    # Constants
    FTP_HOST="ftp.zakupki.gov.ru"
    FTP_USER="free"
    FTP_PASS="free"
    FTP_FILE="/path.to/file.txt"
    FTP_DIR="fcs_regions"
    connFTP = FTP(ftpSource = FTP_HOST, userSource = FTP_USER, passSource = FTP_PASS)
    #print('print ===  ', connFTP.getDirectory())
    #print('print ===  ', connFTP.getDirectory(FTP_DIR))
    newDir = FTP_DIR + '/Moskva/contracts/*.zip'
    #print('print ===  ', connFTP.getDirectory(newDir))
    nameFiles = connFTP.getDirectory(newDir)
    print('Kol files = ', len(nameFiles))
    # connFTP.getFile(fromFile = FTP_DIR + '/Moskva/contracts/contract_Moskva_2022050100_2022060100_217.xml.zip', 
    #                 toFile = '/media/al/BigData/Projects_My/python_workshops/interesting_libraries/tempfile/')
    print(connFTP.getSizeFile(nameFile = FTP_DIR + '/Moskva/contracts/contract_Moskva_2022050100_2022060100_217.xml.zip'))

if __name__ == '__main__':
    test1()


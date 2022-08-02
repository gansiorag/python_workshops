'''
 This module make how depending index element list if two element equwalent
    
Athor: Gansior Alexander, gansior@gansior.ru, +79173383804
Starting 2022//
Ending 2022//
    
'''
from termcolor import colored # manadger style print in console


def prog1():
    pass
    
    
def prog2():
    pass
    
    
if __name__ == '__main__':
    listProba = ['a','b', 'c', 'd', 'b', 'g']
    print(colored(' ====== Start experiment =======', 'red'))
    for simb in listProba:
        print(simb, listProba.index(simb), sep=' ===> ')
    print(colored(' ====== The end =======', 'red'))
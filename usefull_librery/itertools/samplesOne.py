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
    
import itertools
    
def prog1():
    """
    Модуль itertools стандартизирует основной набор быстрых эффективных по 
    памяти инструментов, которые полезны сами по себе или в связке с другими 
    инструментами. Вместе они формируют «алгебру итераторов», которая позволяет 
    лаконично и эффективно создавать специализированные инструменты 
    на чистом Python.
    Модуль itertools находится в стандартной библиотеке Python.
    
    Модуль представляет следующие типы итераторов: 
    Бесконечные итераторы;
    Конечные итераторы;
    Комбинаторные генераторы.
    
    Возвращаемый объект также будет итератором. Мы можем проходиться по 
    итератору с помощью:
    функции «next»
    цикла for
    конвертации в список с помощью list()

    Бесконечные итераторы:
    count(), cycle(), repeat()

    1. count()

        Создает итератор, который возвращает равномерно распределенные значения, 
        начиная с числа, указанного в аргументе start. По умолчанию start равен 0, 
        а step -1. Шаг также может быть нецелым значением. 
        Эта функция вернет бесконечный итератор.
    """
    cc = itertools.count(10, 2)
    print('Step 1 --- '*3)
    cprint(f'{next(cc)}' , 'red', attrs=['bold'])
    cprint(f'{next(cc)}' , 'red', attrs=['bold'])
    cprint(f'{next(cc)}' , 'red', attrs=['bold'])
    cprint(f'{next(cc)}' , 'red', attrs=['bold'])
    print()
    print('Step 2 --- '*3)
    cprint('='*20, 'blue')
    print()
    l1=[5,15,25]
    l2=zip(itertools.count(),l1)
    #It will return zip object which is an iterable instance of zip class
    print (l2)
    print (list(l2))
    #accessing values in the iterator using for loop.step argument can be float values also.
    c2=itertools.count(2.5,2.5)
    for i in c2:
        #including terminating condition, else loop will keep on going.(infinite loop)
        if i>25:
            break
        else:
            print (i,end=" ") #Output:2.5 5.0 7.5 10.0 12.5 15.0 17.5 20.0 22.5 25.0
            

    #step can be negative numbers also.negative numbers count backwards.
    c3=itertools.count(2,-2.5)
    print (next(c3))#Output:2
    print (next(c3))#Output:-0.5
    print (next(c3))#Output:-3.0
    
    
def prog2():
    pass
    
    
if __name__ == '__main__':
    name=''
    prog1()
    prog2()
'''
 This module make exampel function for checks pytest
    
Athor: Gansior Alexander, gansior@gansior.ru, +79173383804
Starting 2022//
Ending 2022//
    
'''

from collections import namedtuple
Task = namedtuple('Task', ['summary', 'owner', 'done', 'id'])
Task.__new__.__defaults__ = (None, None, False, None)
    
def test_defaults():
    """
    Использование параметров не должно вызывать знаения по умолчанию.
    """
    t1 = Task()
    t2 = Task(None, None, False, None)
    assert t1 == t2
    
    
def test_member_access():
    """Проверка своства .field (поля) namedtuple
    """
    t = Task('buy milk', 'brain')
    assert t.summary == 'buy milk'
    assert t.owner == 'brain'
    assert (t.done, t.id) == (False, None)

"""Module providing a function decorators of printing with add fragments AAAAAA !!!!!."""


def decor_one(func):
    """AI is creating summary for decor_one

    Args:
        func ([type]): [description]
    """
    def inner():
        print()
        print('inner')
        print()
        ex_func = 'AAAAAA !!!!!   ' + func()
        return print(ex_func)
    return inner

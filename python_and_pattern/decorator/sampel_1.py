def decor_one(func):
    def inner():
        print()
        print('inner')
        print()
        ex_func = 'AAAAAA !!!!!   ' + func()
        return print(ex_func)
    return inner


@decor_one
def print_hello():
    print("Hello!!!!", end=' ')
    return 'Alex!!!'


print_hello()
print('End!!!')

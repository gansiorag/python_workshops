import inspect


def f1():
    global x
    x = 10
    print(x)
    x = 20
    print(x)
    frame = inspect.currentframe()
    print()
    print(frame.f_back.f_locals)
    print()
    print(frame)


if __name__ == "__main__":
    print('__name__ == ', __name__)
    f1()

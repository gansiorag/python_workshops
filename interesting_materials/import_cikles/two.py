# two.py
import one              # раньше: from one import func_one

def do_work():
    one.func_one()      # раньше: func_one()

def func_two():
    print("Hello, world!")

# https://habr.com/ru/articles/944684/

import two  # раньше: from two import func_two

def func_one():
    two.func_two()      # раньше: func_two()

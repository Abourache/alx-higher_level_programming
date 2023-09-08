#!/usr/bin/python3
from magic_calculation_102 import add, sub
def magic_calculation(a, b):
    if a < b:
        s = add(a, b)
        for i in range(4, 6):
            s = add(s, i)
            return s
    else:
        r = sub(a, b)
        return r

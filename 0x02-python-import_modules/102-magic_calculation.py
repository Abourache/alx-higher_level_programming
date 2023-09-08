#!/usr/bin/python3
def magic_calculation(a, b):
    if a < b:
        s = add(a, b)
        for i in range(4, 6):
            s = add(s, i)
            return s
    else:
        r = sub(a, b)
        return r

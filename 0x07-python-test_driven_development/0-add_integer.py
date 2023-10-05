#!/usr/bin/python3
"""
This is the addition module.
it adds 2 integers
a and b must be first casted
"""



def add_integer(a, b=98):
    """a and are integers
    Returns an integer: the addition of a and b
    """

    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    elif type(b) not in (int, float):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)

    if __name__ == "__main__":
        import doctest
        doctest.testfile("tests/0-add_integer.txt")

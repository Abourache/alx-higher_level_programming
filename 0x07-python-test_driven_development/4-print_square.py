#!/usr/bin/python3
"""
Print Square module, for printing squares with "#".

useful for all square-based applications
"""


def print_square(size):
    """size is the size length of the square
    size must be an integer
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print('#', end='')
        print()

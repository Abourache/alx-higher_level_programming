#!/usr/bin/python3
"""
append_write module
"""


def append_write(filename="", text=""):
    """ function that appends a string returns the number of characters """

    with open(filename, mode="a", encoding="UTF-8") as f:
        return (f.write(text))

#!/usr/bin/python3
"""
text identation module:
indents text
useful
"""


def text_indentation(text):
    """text must be a string, There should be no space
    at the beginning
    or at the end of each printed line.
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    for delim in ".:?":
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])

    print("{}".format(text), end="")

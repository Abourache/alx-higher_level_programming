#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for l, v in list(a_dictionary.items()):
        if v is value:
            a_dictionary.pop(l)
    return a_dictionary

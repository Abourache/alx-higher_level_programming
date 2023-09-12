#!/usr/bin/python3
def no_c(my_string):
    liststr = list(my_string)
    for char in liststr:
        if char == 'c' or char == 'C':
            liststr.remove(char)
    return("".join(liststr))

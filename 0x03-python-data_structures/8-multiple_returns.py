#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        my_tu = (0, None)
    else:
        my_tu = (len(sentence), sentence[:1])
    return(my_tu)
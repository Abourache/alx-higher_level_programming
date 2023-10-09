#!/usr/bin/python3
"""module with method is_same_class"""


def is_same_class(obj, a_class):
    """Returns:
    True: if the object is exactly an instance of the specified class
    False: otherwise"""
    return type(obj) == a_class

#!/usr/bin/python3
"""module with method inherits_from"""


def inherits_from(obj, a_class):
    """Method that return True if an object is an instance of a class
    that inherited from"""
    return isinstance(obj, a_class) and type(obj) != a_class

#!/usr/bin/python3
"""Defines a class Square"""
class Square:
    """
    Class that defines properties of square.

    Attributes:
        size: size of a square.
    """
        def __init__(self, size=0):
            """Creates new instances of square.

            Args:
                size: size of the square.
            """
                self.__size = size
                if type(size) != int:
                        raise TypeError("size must be an integer")
                if size < 0:
                        raise ValueError("size must be >= 0")

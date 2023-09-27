#!/usr/bin/python3
"""Defines a class Square"""
class Square:
    """
    Class that defines properties of square.

    Attributes:
        size: size of a square (1 side).
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

        def area(self):
            """Calculates the area of square.

            Returns: the current square area.
            """
                return self.__size**2
        
        @property
        def size(self):
            """Returns the size of a square"""
                return self.__size

        @size.setter
        def size(self, value):
            """Property setter for size.

            Args:
                value (int): size of a square .

            Raises:
                TypeError: size must be an integer
                ValueError: size must be >= 0
            """
                self.__size = value
                if type(value) != int:
                        raise TypeError("size must be an integer")
                if value < 0:
                        raise ValueError("size must be >= 0")

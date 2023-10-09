#!/usr/bin/python3
"""Module with class MyList"""


class MyList(list):
    """MyList class - Inherits from list"""
    def print_sorted(self):
        """Prints a sorted list"""
        print(sorted(self))

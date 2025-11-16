#!/usr/bin/python3
"""
This module defines the MyList class, which inherits from list.
"""


class MyList(list):
    """
    A class that inherits from list and adds a sorted printing method.

    Methods:
        print_sorted(self): Prints the list in ascending sorted order.
    """

    def print_sorted(self):
        """
        Prints the elements of the list in ascending sorted order.

        The original list is not modified.
        Assumes all elements of the list are of type int.
        """
        # sorted() returns a new sorted list without modifying the original
        print(sorted(self))

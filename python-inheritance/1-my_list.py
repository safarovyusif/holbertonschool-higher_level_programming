#!/usr/bin/python3
"""Defines a custom list class that adds a method for sorted printing."""


class MyList(list):
    """
    MyList class inherits from list.

    It provides one public instance method: print_sorted, which prints
    the list elements in ascending order without modifying the original list.
    """

    def print_sorted(self):
        """
        Prints the list in ascending order.

        It uses the built-in 'sorted()' function to create a new, sorted
        list for printing, ensuring the original list instance remains
        unchanged. Assumes all elements in the list are integers.
        """
        # sorted() returns a new sorted list, keeping the original self intact.
        print(sorted(self))

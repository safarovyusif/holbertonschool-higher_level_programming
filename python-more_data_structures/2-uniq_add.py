#!/usr/bin/python3
"""
2-uniq_add.py
Add all unique integers in a list (each integer counted once).
"""


def uniq_add(my_list=[]):
    """
    Return the sum of all unique integers in my_list.
    """
    return sum(set(my_list))

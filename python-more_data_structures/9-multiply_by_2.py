#!/usr/bin/python3
"""
9-multiply_by_2.py
Return a new dictionary with all values multiplied by 2.
"""


def multiply_by_2(a_dictionary):
    """
    Return a new dictionary where each value from a_dictionary is multiplied
    by 2. The original dictionary is not modified.
    """
    return {key: value * 2 for key, value in a_dictionary.items()}

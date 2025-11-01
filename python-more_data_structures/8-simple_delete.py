#!/usr/bin/python3
"""
8-simple_delete.py
Delete a key in a dictionary if it exists and return the dictionary.
"""


def simple_delete(a_dictionary, key=""):
    """
    Remove key from a_dictionary if present.
    Return the (possibly modified) dictionary.
    """
    a_dictionary.pop(key, None)
    return a_dictionary

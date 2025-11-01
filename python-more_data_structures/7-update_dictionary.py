#!/usr/bin/python3
"""
7-update_dictionary.py
Replace or add key/value in a dictionary and return the dictionary.
"""


def update_dictionary(a_dictionary, key, value):
    """
    Update a_dictionary by setting a_dictionary[key] = value.
    Return the updated dictionary.
    """
    a_dictionary[key] = value
    return a_dictionary

#!/usr/bin/python3
"""
10-best_score.py
Return the key with the highest integer value in a dictionary.
"""


def best_score(a_dictionary):
    """
    Return the key with the biggest integer value in a_dictionary.
    If a_dictionary is None or empty, return None.
    """
    if not a_dictionary:
        return None
    return max(a_dictionary, key=a_dictionary.get)

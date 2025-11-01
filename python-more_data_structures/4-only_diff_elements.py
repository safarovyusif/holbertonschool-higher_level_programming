#!/usr/bin/python3
"""
4-only_diff_elements.py
Return a set of all elements present in only one set.
"""


def only_diff_elements(set_1, set_2):
    """
    Return a new set with elements that are in exactly one of the two sets.
    """
    return set_1 ^ set_2

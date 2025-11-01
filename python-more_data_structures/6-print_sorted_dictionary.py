#!/usr/bin/python3
"""
6-print_sorted_dictionary.py
Print a dictionary by ordered keys (alphabetical order).
"""


def print_sorted_dictionary(a_dictionary):
    """
    Print the dictionary's key/value pairs sorted by key (alphabetical).
    Only first-level keys are sorted. Values are printed as-is.
    """
    for key in sorted(a_dictionary.keys()):
        print("{}: {}".format(key, a_dictionary[key]))

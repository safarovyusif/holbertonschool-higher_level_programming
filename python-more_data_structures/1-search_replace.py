#!/usr/bin/python3
"""
1-search_replace.py
Replace all occurrences of an element by another in a new list.
"""


def search_replace(my_list, search, replace):
    """
    Replace occurrences of search with replace in a new list.
    """
    return [replace if item == search else item for item in my_list]

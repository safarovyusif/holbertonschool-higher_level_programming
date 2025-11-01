#!/usr/bin/python3
"""
1-search_replace.py
Replace all occurrences of an element by another in a new list.
"""

def search_replace(my_list, search, replace):
    """
    my_list: list of elements
    search: element to replace
    replace: new element
    Returns a new list where every occurrence of search is replaced by replace.
    The original list is not modified.
    """
    return [replace if item == search else item for item in my_list]

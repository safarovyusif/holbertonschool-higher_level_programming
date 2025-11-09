#!/usr/bin/python3
"""
This module provides a function that adds two integers.
It ensures inputs are either integers or floats.
If inputs are invalid, a TypeError is raised.
Floats are first casted to integers before addition.
"""


def add_integer(a, b=98):
    """Add two integers or floats and return the result as integer."""
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))

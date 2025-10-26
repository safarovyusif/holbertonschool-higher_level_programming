#!/usr/bin/python3
def islower(c):
    """Return True if c is a lowercase letter, otherwise False."""
    return isinstance(c, str) and len(c) == 1 and ord('a') <= ord(c) <= ord('z')

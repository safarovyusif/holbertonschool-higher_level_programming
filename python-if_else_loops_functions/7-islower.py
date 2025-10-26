#!/usr/bin/python3
def islower(c):
    """Return True if c is a lowercase ASCII letter, False otherwise."""
    if not isinstance(c, str) or len(c) != 1:
        return False
    code = ord(c)
    return ord('a') <= code <= ord('z')

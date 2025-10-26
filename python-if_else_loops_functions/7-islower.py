#!/usr/bin/python3
def islower(c):
    return isinstance(c, str) and len(c) == 1 and ord('a') <= ord(c) <= ord('z')

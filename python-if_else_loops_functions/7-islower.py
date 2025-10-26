#!/usr/bin/python3
def uppercase(str):
    res = ""
    for c in str:
        o = ord(c)
        if 97 <= o <= 122:
            res += chr(o - 32)
        else:
            res += c
    print("{}".format(res))

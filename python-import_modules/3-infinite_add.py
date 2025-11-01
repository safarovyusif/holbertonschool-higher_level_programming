#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    i = 0
    sum = 0
    argc = len(argv)
    if argc == 1:
        print("0")
    else:
        for i in range(1, argc):
            i = int(argv[i])
            sum = sum + i
        print("{}".format(sum))

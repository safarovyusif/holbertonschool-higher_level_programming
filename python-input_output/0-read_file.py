#!/usr/bin/python3
"""
Module for reading a text file and printing its contents to stdout.
This module contains a single function that reads a UTF-8 file and prints it.
"""


def read_file(filename=""):
    """
    Read a text file (UTF-8) and print its contents to stdout.
    Args:
        filename (str): name of the file to read.
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")

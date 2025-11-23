#!/usr/bin/python3
"""
Module containing a function that writes text to a UTF-8 file.
The file is overwritten if it already exists.
"""


def write_file(filename="", text=""):
    """
    Write a string to a text file (UTF-8) and return
    the number of characters written.

    Args:
        filename (str): The name of the file to write into.
        text (str): The string to write into the file.

    Returns:
        int: Number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)

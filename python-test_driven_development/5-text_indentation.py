#!/usr/bin/python3
"""
This module has one function that adds two new lines
after each '.', '?', or ':' in a given text.
"""


def text_indentation(text):
    """
    Prints text with 2 new lines after '.', '?' and ':' characters.

    Args:
        text (str): The text to be printed.

    Raises:
        TypeError: If text is not a string.
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    result = text[:]

    for mark in ".?:":
        parts = result.split(mark)
        result = ""
        for part in parts:
            part = part.strip(" ")
            if result == "":
                result = part + mark
            else:
                result += "\n\n" + part + mark

    print(result[:-3], end="")

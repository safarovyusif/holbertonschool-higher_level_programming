#!/usr/bin/python3
"""This file makes a Square class."""


class Square:
    """A class that stands for a square."""

    def __init__(self, size=0):
        """
        Start a new square.

        Args:
            size (int): The size of the square (default is 0).
        Raises:
            TypeError: If size is not an int.
            ValueError: If size is smaller than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

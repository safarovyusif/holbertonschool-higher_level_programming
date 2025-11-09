#!/usr/bin/python3
"""This module creates a Square class."""


class Square:
    """A simple class that describes a square."""

    def __init__(self, size=0):
        """
        Create a new Square.

        Args:
            size (int): length of the square's side (default is 0).
        Raises:
            TypeError: if size is not an integer.
            ValueError: if size is negative.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

#!/usr/bin/python3
"""Square class with private size."""


class Square:
    """Class that defines a square by its size."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size: size of the square.
        """
        self.__size = size

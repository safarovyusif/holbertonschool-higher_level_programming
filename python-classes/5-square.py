#!/usr/bin/python3
"""Simple class that shows a square."""


class Square:
    """A class that makes a square."""

    def __init__(self, size=0):
        """
        Create a new square.

        Args:
            size (int): side length (default is 0).
        """
        self.size = size

    @property
    def size(self):
        """Get the side length."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Change the side length.

        Args:
            value (int): new length.
        Raises:
            TypeError: if value is not an int.
            ValueError: if value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square using # character."""
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__size):
                print("#" * self.__size)

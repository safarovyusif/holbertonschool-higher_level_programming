#!/usr/bin/python3
"""Simple class that shows a square."""


class Square:
    """A class that creates and prints a square."""

    def __init__(self, size=0, position=(0, 0)):
        """
        Make a new square.

        Args:
            size (int): side length (default is 0).
            position (tuple): space before printing (default is (0, 0)).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get the side length."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set a new side length.

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

    @property
    def position(self):
        """Get the print position."""
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set a new print position.

        Args:
            value (tuple): two positive integers.
        Raises:
            TypeError: if value is not a tuple of 2 positive ints.
        """
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(num, int) for num in value)
            or not all(num >= 0 for num in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with # using its position."""
        if self.__size == 0:
            print("")
            return

        # Print blank lines for vertical space
        for _ in range(self.__position[1]):
            print("")

        # Print rows with spaces for horizontal space, then #
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

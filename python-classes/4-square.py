#!/usr/bin/python3
"""This module defines a Square class that can print a square."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initializes a square with a private validated size."""
        self.size = size

    @property
    def size(self):
        """Retrieves the square size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the square size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square using the # character."""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)

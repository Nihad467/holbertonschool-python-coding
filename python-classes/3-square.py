#!/usr/bin/python3
"""This module defines a Square class with property access."""


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

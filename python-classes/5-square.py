#!/usr/bin/python3
"""This module defines a class Square."""


class Square:
    """This class prints a square."""

    def __init__(self, size=0):
        """Initializes a square with an optional size."""
        self.size = size

    @property
    def size(self):
        """Retrieves the size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size attribute with type and value validation."""
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Calculates and returns the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with character #."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print('#' * self.__size)

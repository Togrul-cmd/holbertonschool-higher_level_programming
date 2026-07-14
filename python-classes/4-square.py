#!/usr/bin/python3
"""This module defines a class Square."""


class Square:
    """This class defines a square with a property."""
    def __init__(self, size=0):
        """Initialized with optional size."""
        self.size = size

    @property
    def size(self):
        """This is property for size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size attribute with type and size validation."""
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """This method calculates square area."""
        area = self.__size ** 2
        return area

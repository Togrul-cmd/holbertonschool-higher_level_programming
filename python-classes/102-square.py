#!/usr/bin/python3
"""This module defines a class Square."""


class Square:
    """This class defines a square with a property and special methods."""
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
        if type(value) is not int and type(value) is not float:
            raise TypeError('size must be a number')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """This method calculates square area."""
        area = self.__size ** 2
        return area

    def __lt__(self, other):
        """Returns true if self.area is less than other.area."""
        return self.area() < other.area()

    def __gt__(self, other):
        """Returns true if self.area is greater than other.area"""
        return self.area() > other.area()

    def __eq__(self, other):
        """Returns true if self.area is equal to other.area."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Returns true if self.area is not equal to other.area."""
        return self.area() != other.area()

    def __le__(self, other):
        """Returns true if self.area <= other.area."""
        return self.area() <= other.area()

    def __ge__(self, other):
        """Returns true if self.area >= other.area."""
        return self.area() >= other.area()

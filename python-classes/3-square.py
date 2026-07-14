#!/usr/bin/python3
"""This module defines a class Square."""


class Square:
    """This class defines a square with a method to find its area."""
    def __init__(self, size=0):
        """size must be a non-negative integer if provided."""
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
    
    def area(self):
        """This method calculates area of the square."""
        area = self.__size ** 2
        return area

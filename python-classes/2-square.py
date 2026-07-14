#!/usr/bin/python3
"""This module defines a class Square."""


class Square:
    """This class defines an object square with private attribute size.

    Attributes:
        __size (int): Should be a positive integer.
    """
    def __init__(self, size=0):
        """size parameter must be a positive integer if provided."""
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

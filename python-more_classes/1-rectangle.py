#!/usr/bin/python3
"""This module defines a class Rectangle."""


class Rectangle:
    """Defines rectangle object wiht width and height attributes."""
    def __init__(self, width=0, height=0):
        """Instantiates with optional width and height."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Checks value type and sets width."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Checks value and sets height."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

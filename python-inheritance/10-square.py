#!/usr/bin/python3
"""This module defines class Rectangle that inherits BaseGeometry."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Inherits Rectangle."""
    def __init__(self, size):
        self.integer_validator('size', size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Calculates and returns area of square."""
        return super().area()

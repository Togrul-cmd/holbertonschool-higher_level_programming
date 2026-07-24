#!/usr/bin/env python3
"""
Module defining an abstract Shape class and two subclasses.
"""

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """Abstract Shape class."""

    @abstractmethod
    def area(self):
        """Calculates area."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculates perimeter."""
        pass


class Circle(Shape):
    """Circle class inheriting from Shape."""

    def __init__(self, radius):
        """Initializes a Circle."""
        self.radius = radius

    def area(self):
        """Calculates the area of the circle."""
        return pi * self.radius ** 2

    def perimeter(self):
        """Calculates the perimeter of the circle."""
        return 2 * pi * self.radius


class Rectangle(Shape):
    """Rectangle class inheriting from Shape."""

    def __init__(self, width, height):
        """Initializes a Rectangle."""
        self.width = width
        self.height = height

    def area(self):
        """Calculates the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculates the perimeter of the rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Prints the area and perimeter of a shape."""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")

if __name__ == '__main__':
    obj_1 = Circle(5)
    obj_2 = Rectangle(2, 3)

    shape_info(obj_1)
    shape_info(obj_2)

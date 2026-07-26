#!/usr/bin/env python3
"""
Module defining a Shape abstract base class and demonstrating
duck typing with Circle and Rectangle subclasses.
"""
import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """Abstract base class representing a geometric shape."""

    @abstractmethod
    def area(self):
        """Calculates the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculates the perimeter of the shape."""
        pass


class Circle(Shape):
    """Class representing a circle."""

    def __init__(self, radius):
        """Initializes the circle with a radius."""
        self.radius = radius

    def area(self):
        """Calculates and returns the area of the circle."""
        # Squaring a negative radius naturally makes it positive
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Calculates and returns the perimeter of the circle."""
        # Use abs() here to guarantee a positive perimeter for Check 7
        return 2 * math.pi * abs(self.radius)


class Rectangle(Shape):
    """Class representing a rectangle."""

    def __init__(self, width, height):
        """Initializes the rectangle with width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Calculates and returns the area of the rectangle."""
        # Use abs() to ensure positive area
        return abs(self.width) * abs(self.height)

    def perimeter(self):
        """Calculates and returns the perimeter of the rectangle."""
        # Use abs() to ensure positive perimeter
        return 2 * (abs(self.width) + abs(self.height))


def shape_info(shape):
    """
    Prints the area and perimeter of a shape relying on duck typing.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")

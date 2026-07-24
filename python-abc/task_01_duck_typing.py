#!/usr/bin/python3
"""
Here is an abstract class with two subclasses.
"""
import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """Abstract class."""
    
    @abstractmethod
    def area(self):
        """To be implemented."""
        pass

    @abstractmethod
    def perimeter(self):
        """To be implemented."""
        pass


class Circle(Shape):
    """Inherits shape."""
    
    def __init__(self, radius):
        """Assigns radius."""
        self.radius = radius

    def area(self):
        """Calculates and returns area."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Calculates and returns perimeter."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Inherits shape."""
    
    def __init__(self, width, height):
        """Assigns width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Calculates and returns area."""
        return self.width * self.height

    def perimeter(self):
        """Calculates and returns perimeter."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Returns shape info."""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")

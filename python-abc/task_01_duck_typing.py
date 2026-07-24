#!/usr/bin/python3
"""
    Here is abstract class with two subclasses.
"""
from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """Abstract class."""
    @abstractmethod
    def area(self): ...

    @abstractmethod
    def perimeter(self): ...


class Circle(Shape):
    """Inherits shape."""
    def __init__(self, radius):
        """Assigns radius."""
        self.radius = radius

    def area(self):
        """Calcualtes and returns area."""
        return pi * self.radius ** 2

    def perimeter(self):
        """Calculates and returns perimeter."""
        return 2 * pi * self.radius


class Rectangle(Shape):
    """Inherits shape."""
    def __init__(self, width, height):
        """Assigns radius."""
        self.width = width
        self.height = height

    def area(self):
        """Calcualtes and returns area."""
        return self.width * self.height

    def perimeter(self):
        """Calculates and returns perimeter."""
        return 2 * (self.height + self.width)


def shape_info(shape):
    """Returns shape info."""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")


if __name__ == "__main__":
    # Instantiate a Circle and a Rectangle
    my_circle = Circle(5)
    my_rectangle = Rectangle(4, 6)
# Pass each object to the shape_info function
    print("Circle Info:")
    shape_info(my_circle)
    
    print("Rectangle Info:")
    shape_info(my_rectangle)
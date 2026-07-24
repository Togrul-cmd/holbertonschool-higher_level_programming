#!/usr/bin/python3
"""
    This module defines abstract class
    and two subclasses.
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """This is an abstract class."""
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """Inherits from Animal."""
    def sound(self):
        """Implements sound from parent class."""
        return "Bark"


class Cat(Animal):
    """Inherits from Animal."""
    def sound(self):
        """Implements sound from parent class."""
        return "Meow"

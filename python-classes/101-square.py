#!/usr/bin/python3
"""This module defines class Square similar to <6-square.py>."""


class Square:
    """This class defines printable square object."""
    def __init__(self, size=0, position=(0,0)):
        """Initializes square object with size and position."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieves size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets size attribute with validation."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Retrieves position attribute."""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets position attribute with validation."""
        if (type(value) is not tuple or len(value) != 2 or
            type(value[0]) is not int or value[0] < 0 or
            type(value[1]) is not int or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integer")
        self.__position = value

    def area(self):
        """Calculates and returns area of a square."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the character "#"."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(' ' * self.__position[0] + '#' * self.__size)

    def __str__(self):
        """Has the same behaviour as my_print."""
        res = []
        if self.__size == 0:
            return ''
        else:
            for _ in range(self.__position[1]):
                res.append('')
            for _ in range(self.__size):
                res.append(' ' * self.__position[0] + '#' * self.__size)
        return '\n'.join(res)

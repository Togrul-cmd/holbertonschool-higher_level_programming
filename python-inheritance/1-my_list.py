#!/usr/bin/python3
"""This module defines a class MyList inheriting List."""


class MyList(list):
    """This class inherits list and prints sorted list."""
    def print_sorted(self):
        """Prints sorted list."""
        print(sorted(self))

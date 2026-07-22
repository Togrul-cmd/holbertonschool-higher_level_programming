#!/usr/bin/python3
"""This module defines MyInt class derived from int."""


class MyInt(int):
    """Rebel int child class."""
    def __eq__(self, other):
        """Inverted equality."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Inverted non-equality."""
        return super().__eq__(other)

#!/usr/bin/env python3
"""
    This module defines a function
    that finds a transpose of 2d matrix.
"""


def matrix_transpose(matrix):
    """Returns the transpose of a 2D matrix."""
    return [list(row) for row in zip(*matrix)]

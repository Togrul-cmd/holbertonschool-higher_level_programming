#!/usr/bin/env python3
"""
    Module to perform
    element-wise addition, subtraction, multiplication, and division.
"""


def np_elementwise(mat1, mat2):
    """Element-wise addition, subtraction, multiplication, and division."""
    add = mat1 + mat2
    subtraction = mat1 - mat2
    multiplication = mat1 * mat2
    division = mat1 / mat2
    return add, subtraction, multiplication, division

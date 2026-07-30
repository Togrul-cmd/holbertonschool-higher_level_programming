#!/usr/bin/env python3
"""This module defines square summing function."""


def summation_i_squared(n):
    """Calculates and returns the sum of first n numbers."""
    if type(n) is not int or n < 1:
        return None
    return n * (n + 1) * (2 * n + 1) // 6

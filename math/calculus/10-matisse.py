#!/usr/bin/env python3
"""
    This module defines a function that
    calculates the derivative of a polynomial.
"""


def poly_derivative(poly):
    """calculates and returns the derivative of a polynomial."""
    if not isinstance(poly, list) or len(poly) == 0:
        return None
    
    for coef in poly:
        if type(coef) not in (int, float):
            return None
    
    if len(poly) == 1:
        return [0]

    return [i * poly[i] for i in range(1, len(poly))]

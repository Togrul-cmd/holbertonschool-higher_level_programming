#!/usr/bin/env python3
"""Module to add two matrixes."""


def add_matrices(mat1, mat2):
    """Adds 2 matrixes."""
    if not isinstance(mat1, list) and not isinstance(mat2, list):
        return mat1 + mat2
    if not isinstance(mat1, list) or not isinstance(mat2, list)
    or len(mat1) != len(mat2):
        return None
    result = []
    for add1, add2 in zip(mat1, mat2):
        sub_result = add_matrices(add1, add2)
        if sub_result is None:
            return None
        result.append(sub_result)
    return result

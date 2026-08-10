#!/usr/bin/env python3
"""Module to add two matrixes."""


def formatting(lst):
    if isinstance(lst, list) and None in lst:
        return None
    return lst


def add_matrices(mat1, mat2):
    if not isinstance(mat1, list) and not isinstance(mat2, list):
        return mat1 + mat2
    if not isinstance(mat1, list) or not isinstance(mat2, list)
    or len(mat1) != len(mat2):
        return None
    return formatting([add_matrices(add1, add2) for
                       add1, add2 in zip(mat1, mat2)])

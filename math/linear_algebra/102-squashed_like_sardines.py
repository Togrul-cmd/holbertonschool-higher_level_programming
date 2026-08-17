#!/usr/bin/env python3
"""Module to concatenate two matrices along a specific axis."""


def cat_matrices(mat1, mat2, axis=0):
    """Concatenate two matrices along a specific axis."""
    if not isinstance(mat1, list) or not isinstance(mat2, list):
        return None
    if axis == 0:
        if isinstance(mat1[0], list) and isinstance(mat2[0], list):
            if cat_matrices(mat1[0], mat2[0], axis=0) is None:
                return None
        elif isinstance(mat1[0], list) != isinstance(mat2[0], list):
            return None
        return mat1 + mat2
    if len(mat1) != len(mat2):
        return None
    result = []
    for cat1, cat2 in zip(mat1, mat2):
        sub_result = cat_matrices(cat1, cat2, axis - 1)
        if sub_result is None:
            return None
        result.append(sub_result)
    return result

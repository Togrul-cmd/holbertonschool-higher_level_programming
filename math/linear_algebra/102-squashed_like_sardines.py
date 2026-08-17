#!/usr/bin/env python3
"""Module to concatenate two matrices along a specific axis."""


def shape(matrix):
    """Calculates the shape of an N-dimensional matrix."""
    matrix_shape = []
    curr = matrix
    while isinstance(curr, list):
        matrix_shape.append(len(curr))
        if len(curr) == 0:
            break
        curr = curr[0]
    return tuple(matrix_shape)


def cat_matrices(mat1, mat2, axis=0):
    """Concatenates two N-dimensional matrices along a given axis."""
    if not isinstance(mat1, list) or not isinstance(mat2, list):
        return None

    s1 = shape(mat1)
    s2 = shape(mat2)

    # 1. Both matrices must have the same number of dimensions
    if len(s1) != len(s2):
        return None

    # 2. Axis must be within bounds
    if axis < 0 or axis >= len(s1):
        return None

    # 3. All dimensions EXCEPT `axis` must match exactly
    for i in range(len(s1)):
        if i != axis and s1[i] != s2[i]:
            return None

    # Recursive helper to perform concatenation
    def concat_recursive(m1, m2, curr_axis):
        if curr_axis == 0:
            return m1 + m2

        result = []
        for sub1, sub2 in zip(m1, m2):
            result.append(concat_recursive(sub1, sub2, curr_axis - 1))
        return result

    return concat_recursive(mat1, mat2, axis)

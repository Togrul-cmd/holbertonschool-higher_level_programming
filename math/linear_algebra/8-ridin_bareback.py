#!/usr/bin/env python3
"""Module to perform matrix multiplication."""


def mat_mul(mat1, mat2):
    """Multiplies two 2D matrices."""
    if len(mat1[0]) != len(mat2):
        return None
    res = []
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat2[0])):
            total = 0
            for k in range(len(mat2)):
                total += mat1[i][k] * mat2[k][j]
            row.append(total)
        res.append(row)
    return res

#!/usr/bin/env python3
"""Module to slice a matrix along specific axes."""
import numpy as np


def np_slice(matrix, axes={}):
    """Slices a numpy ndarray along specified axes using a dictionary."""
    slices = [
        slice(*axes[i]) if i in axes else slice(None)
        for i in range(matrix.ndim)
    ]
    return matrix[tuple(slices)]

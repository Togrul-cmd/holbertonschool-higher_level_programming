#!/usr/bin/env python3
"""Definiteness functions"""

import numpy as np


def definiteness(matrix):
    """
    Definiteness function
    Args:
        matrix: numpy.ndarray of shape (n, n)
                whose definiteness should be calculated
    Returns: positive definite, positive semi-definite,
             negative semi-definite, negative definite of
             indefinite, respectively
    """
    if not isinstance(matrix, np.ndarray):
        raise TypeError("matrix must be a numpy.ndarray")
    if len(matrix.shape) != 2 or matrix.shape[0] != matrix.shape[1]:
        return None
    if not np.all(matrix.T == matrix):
        return None

    try:
        w, _ = np.linalg.eig(matrix)
    except Exception:
        return None

    if np.all(w > 0):
        return "Positive definite"
    if np.all(w >= 0):
        return "Positive semi-definite"
    if np.all(w < 0):
        return "Negative definite"
    if np.all(w <= 0):
        return "Negative semi-definite"
    return "Indefinite"

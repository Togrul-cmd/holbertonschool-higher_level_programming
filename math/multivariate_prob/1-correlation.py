#!/usr/bin/env python3
""" Calculates a correlation matrix """
import numpy as np


def correlation(C):
    """
    Calculates a correlation matrix from a covariance matrix

    parameters:
        C [np.ndarray of shape (d, d)]: covariance matrix

    returns:
        np.ndarray of shape (d, d) containing the correlation matrix
    """
    if not isinstance(C, np.ndarray):
        raise TypeError("C must be a numpy.ndarray")
    if len(C.shape) != 2 or C.shape[0] != C.shape[1]:
        raise ValueError("C must be a 2D square matrix")

    stddev = np.sqrt(np.diag(C))
    outer_std = np.outer(stddev, stddev)
    corr = C / outer_std

    return corr
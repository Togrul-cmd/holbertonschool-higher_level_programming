#!/usr/bin/env python3
""" Defines the MultiNormal class with PDF calculation """
import numpy as np


class MultiNormal:
    """ Class representing a Multivariate Normal distribution """

    def __init__(self, data):
        """
        Class constructor

        parameters:
            data [np.ndarray of shape (d, n)]: data set
        """
        if not isinstance(data, np.ndarray) or len(data.shape) != 2:
            raise TypeError("data must be a 2D numpy.ndarray")

        d, n = data.shape
        if n < 2:
            raise ValueError("data must contain multiple data points")

        self.mean = np.mean(data, axis=1, keepdims=True)
        data_centered = data - self.mean
        self.cov = np.matmul(data_centered, data_centered.T) / (n - 1)

    def pdf(self, x):
        """
        Calculates the PDF at a specified data point

        parameters:
            x [np.ndarray of shape (d, 1)]: data point

        returns:
            float: value of the PDF at point x
        """
        if not isinstance(x, np.ndarray):
            raise TypeError("x must be a numpy.ndarray")

        d = self.mean.shape[0]
        if x.shape != (d, 1):
            raise ValueError(f"x must have the shape ({d}, 1)")

        det = np.linalg.det(self.cov)
        inv = np.linalg.inv(self.cov)
        diff = x - self.mean

        norm_const = 1.0 / np.sqrt(((2 * np.pi) ** d) * det)
        exponent = -0.5 * np.matmul(np.matmul(diff.T, inv), diff)

        return float(norm_const * np.exp(exponent)[0, 0])

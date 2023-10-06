#!/usr/bin/python3

"""A matrix multiplication function definiiton using NumPy"""
import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """The function to get multiplication of two matrices.

    Args:
        m_a (list of lists of ints/floats): The first
        m_b (list of lists of ints/floats): The second
    """

    return (np.matmul(m_a, m_b))

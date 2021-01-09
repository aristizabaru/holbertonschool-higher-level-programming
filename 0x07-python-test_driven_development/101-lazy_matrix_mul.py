#!/usr/bin/python3
"""Module lazy_matrix_mul

Functions:
    lazy_matrix_mul(m_a, m_b)
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """lazy_matrix_mul()
    multiplies 2 matrices

    Args:
            m_a (matrix): matrix ``A``
            m_b (matrix): matrix ``B``
    Return:
            new_matrix
    """
    return np.matmul(m_a, m_b)

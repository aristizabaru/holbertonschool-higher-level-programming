#!/usr/bin/python3
"""Module matrix_mul

Functions:
    matrix_mul(m_a, m_b)
    check_list(matrix, name)
    check_matrix(matrix, name):
    check_number(matrix, name):
    check_size(matrix, name):
    check_multiply(size_a, size_b):
"""


def matrix_mul(m_a, m_b=0):
    """text_indentation()
    multiplies 2 matrices

    Args:
            m_a (matrix): matrix ``A``
            m_b (matrix): matrix ``B``
    Return:
            new_matrix
    """

    # Check list
    check_list(m_a, "m_a")
    check_list(m_b, "m_b")

    # Check list of list
    check_matrix(m_a, "m_a")
    check_matrix(m_b, "m_b")

    # Check int & float
    check_number(m_a, "m_a")
    check_number(m_b, "m_b")

    # Check sizes of matrix - returns list
    size_a = check_size(m_a, "m_a")
    size_b = check_size(m_b, "m_b")

    # check if they can be multiplied
    check_multiply(size_a, size_b)

    news_matrix = [[sum(a*b for a, b in zip(A_row, B_col))
                    for B_col in zip(*m_b)] for A_row in m_a]

    return news_matrix


def check_list(matrix, name):
    """check_list()
    check if ``matrix`` is a list

    Args:
            matrix (list): list
            name (str): name of the matrix
    Return:
            raise Exception on error
    """
    if type(matrix) is not list:
        raise TypeError("{} must be a list".format(name))
    if len(matrix) == 0:
        raise ValueError("{} can't be empty".format(name))


def check_matrix(matrix, name):
    """check_matrix()
    check if ``matrix`` is a list of list

    Args:
            matrix (list): list
            name (str): name of the matrix
    Return:
            raise Exception on error
    """
    if type(matrix[0]) is not list:
        raise TypeError("{} must be a list of lists".format(name))
    for row in matrix:
        if type(row) is not list:
            raise TypeError("{} must be a list of lists".format(name))
        if len(row) == 0:
            raise ValueError("{} can't be empty".format(name))


def check_number(matrix, name):
    """check_number()
    check if ``matrix`` only have integers or floats

    Args:
            matrix (list): list
            name (str): name of the matrix
    Return:
            raise Exception on error
    """
    valid_types = [int, float]
    for row in matrix:
        for item in row:
            if type(item) not in valid_types:
                raise TypeError(
                    "{} should contain only integers or floats".format(name))


def check_size(matrix, name):
    """check_size()
    check if ``matrix`` rows length is the same

    Args:
            matrix (list): list
            name (str): name of the matrix
    Return:
            raise Exception on error
    """
    base_col = len(matrix[0])
    base_row = len(matrix)
    for row in matrix:
        if base_col != len(row):
            raise TypeError(
                "each row of {} must be of the same size".format(name))

    return [base_row, base_col]


def check_multiply(size_a, size_b):
    """check_multiply()
    check if tow matrix can be multiplied

    Args:
            size_a (list): list with two items representing
                           the number [rows, colums] of a matrix
            nsize_a (list): list with two items representing
                            the number [rows, colums] of a matrix
    Return:
            raise Exception on error
    """
    if size_a[1] != size_b[0]:
        raise ValueError("m_a and m_b can't be multiplied")

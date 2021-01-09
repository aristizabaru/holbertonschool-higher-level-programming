#!/usr/bin/python3
"""Module matrix_divided

Functions:
    matrix_divided(matrix, div)
"""


def matrix_divided(matrix, div):
    """matrix_divided()
    Returns addition of two intergers

    Args:
            matrix (list): a list of values to be divided by `div`
            int (int or float): value that divides each element of matrix
    Return:
            new matrix with elements of `matrix` divided by `div`
            all elements of the new matrix are rounded to 2 decimal places
    """

    # checks for matrix
    if type(matrix) is not list:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        if type(row) is not list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
    if len(matrix) == 0:
        return []
    else:
        base_length = len(matrix[0])
    for row in matrix:
        if len(row) != base_length:
            raise TypeError("Each row of the matrix must have the same size")
        for item in row:
            if type(item) not in [int, float]:
                raise TypeError(
                    "matrix must be a matrix (list of lists) "
                    "of integers/floats")
    # checks for div
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    # division
    new_matrix = list()
    for i, row in enumerate(matrix):
        new_matrix.append([])
        for item in row:
            rounded = "{:.2f}".format(item / div)
            new_matrix[i].append(float(rounded))

    return new_matrix

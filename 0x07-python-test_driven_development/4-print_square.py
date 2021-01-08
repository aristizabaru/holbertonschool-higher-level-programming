#!/usr/bin/python3
"""Module print_square

Functions:
    print_square(size)
"""


def print_square(size):
    """print_square()
    prints a square with the character #

    Size can not be less than 0

    Args:
            size (int): length of the square
    Return:
            nothing
    """
    # checks for size
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    # print square
    for row in range(size):
        print("#" * size, end="")
        print()

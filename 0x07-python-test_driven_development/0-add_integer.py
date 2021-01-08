#!/usr/bin/python3
"""Module add interger

Functions:
    add_integer(a, b)
"""


def add_integer(a, b=98):
    """add_integer()
    Returns addition of two intergers

    Args:
            a (int): value 1
            b (int): value 2
    Return:
            a + b
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a+b

#!/usr/bin/python3
"""Module 2-is_same_class

Functions:
    is_same_class(obj, a_class)
"""


def is_same_class(obj, a_class):
    """Find if an object is exactly an instance of a class

    Arguments:
        obj (object): the object to evaluate
        a_class (class): the class to compare the object

    Return:
        True if the object is exactly an instance of
        the specified class ; otherwise False
    """
    return type(obj) is a_class

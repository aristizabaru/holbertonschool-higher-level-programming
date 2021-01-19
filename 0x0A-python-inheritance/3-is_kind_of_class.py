#!/usr/bin/python3
"""Module 3-is_kind_of_class

Functions:
    is_kind_of_class(obj, a_class)
"""


def is_kind_of_class(obj, a_class):
    """Find if the object is an instance of, or if the object
       is an instance of a class that inherited from, the specified class

    Arguments:
        obj (object): the object to evaluate
        a_class (class): the class to compare the object

    Return:
        True if the object is an instance of, or if the object is an instance
        of a class that inherited from, the specified class ; otherwise False
    """
    return isinstance(obj, a_class)

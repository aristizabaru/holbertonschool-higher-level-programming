#!/usr/bin/python3
"""Module 4-inherits_from

Functions:
    inherits_from(obj, a_class)
"""


def inherits_from(obj, a_class):
    """Find if the object is an instance of a class that inherited
       (directly or indirectly) from the specified class

    Arguments:
        obj (object): the object to evaluate
        a_class (class): the class to compare the object

    Return:
        True if the object is an instance of a class that inherited
        (directly or indirectly) from the specified class ; otherwise False
    """
    if type(obj) is not a_class:
        return issubclass(type(obj), a_class)

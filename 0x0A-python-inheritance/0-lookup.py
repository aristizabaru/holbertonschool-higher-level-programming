#!/usr/bin/python3
"""Module 0-lookup

Functions:
    lookup(obj)
"""


def lookup(obj):
    """Returns the list of available attributes and methods of an object

    Args:
            obj (obj): object to get attributes from

    Return:
            a list object with all the attributes and methods
    """
    return dir(obj)

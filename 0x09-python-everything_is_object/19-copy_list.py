#!/usr/bin/python3
"""19-copy_list module

Functions:
    copy_list(l)
"""


def copy_list(l):
    """copy a list and return a new one

    Arguments:
        l (list): list to be duplicated

    Return:
        copy of `l``
    """
    new_list = l[:]
    return new_list

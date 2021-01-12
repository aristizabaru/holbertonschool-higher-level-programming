#!/usr/bin/python3
"""19-copy_list module

Functions:
    copy_list(lis)
"""


def copy_list(lis):
    """copy a list and return a new one

    Arguments:
        lis (list): list to be duplicated

    Return:
        copy of `lis``
    """
    new_list = lis[:]
    return new_list

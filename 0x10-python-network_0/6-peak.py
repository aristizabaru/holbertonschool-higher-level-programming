#!/usr/bin/python3
"""Find peak in a list and return it

    Functions
        find_peak(list)
"""

def find_peak(list_of_integers):
    """Find peak in a list and return it"""
    if len(list_of_integers) == 0:
        return None
    list_of_integers.sort(reverse=True)
    return list_of_integers[0]
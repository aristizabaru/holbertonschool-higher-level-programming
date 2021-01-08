#!/usr/bin/python3
"""Module say my name

Functions:
    say_my_name(first_name, last_name="")
"""


def say_my_name(first_name, last_name=""):
    """say_my_name()
    Prints My name is <first name> <last name>

    Args:
            first_name (str): first name
            last_name (str): las name
    Return:
            nothing
    """
    # checks for first_name
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    # checks for last_name
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))

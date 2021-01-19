#!/usr/bin/python3
"""Module 101-add_attribute

Function
    add_attribute(obj, attribute, value)
"""


def add_attribute(obj, attribute, value):
    """adds a new attribute to an object if it’s possible

    Arguments:
        obj (object): target object for new attribute
        attribute (str): name of the new attribute
        value (obj): value of the new attribute
    """
    for key in dir(type(obj)):
        if str(key) == "__dict__":
            obj.__dict__[attribute] = value
            return
    raise TypeError("can't add new attribute")

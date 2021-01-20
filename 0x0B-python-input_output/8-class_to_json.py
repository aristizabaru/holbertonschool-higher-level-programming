#!/usr/bin/python3
"""module 8-class_to_json

Functions:
    class_to_json(obj)
"""


def class_to_json(obj):
    """returns a dictionary description with simple data structure
    (list, dictionary, string, integer and boolean) for JSON
    serialization of an object

    Arguments:
        obj (str): object to get attributes from

    Return:
        dictionary with key:value of attributes
    """
    json_dict = dict()
    for attribute in obj.__dict__:
        json_dict[attribute] = obj.__dict__[attribute]
    return json_dict

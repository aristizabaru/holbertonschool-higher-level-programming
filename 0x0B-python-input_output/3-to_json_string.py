#!/usr/bin/python3
"""module 3-to_jason_string

Functions:
     to_json_string(my_obj)
"""
import json


def to_json_string(my_obj):
    """returns the JSON representation of an object (string)

    Arguments:
        my_obj (obj): object that can be serialized

    Return:
        JSON representation (string)
    """
    return json.dumps(my_obj)

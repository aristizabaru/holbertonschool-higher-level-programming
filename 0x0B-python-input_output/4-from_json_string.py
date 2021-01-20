#!/usr/bin/python3
"""module 4-from_json_string

Functions:
    from_json_string(my_str)
"""
import json


def from_json_string(my_str):
    """returns an object (Python data structure)
    represented by a JSON string

    Arguments:
        my_str (str): string that can be deserialized

    Return:
        object
    """
    return json.loads(my_str)

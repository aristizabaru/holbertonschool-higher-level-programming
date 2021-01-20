#!/usr/bin/python3
"""module 6-load_from_json_file

Functions:
    load_from_json_file(filename)
"""
import json


def load_from_json_file(filename):
    """creates an Object from a “JSON file”

    Arguments:
        filename (str): name of file

    Return:
        Object
    """
    with open(filename, mode="r", encoding="utf-8") as fd:
        return json.load(fd)

#!/usr/bin/python3
"""module 5-save_to_json_file

Functions:
    save_to_json_file(my_obj, filename)
"""
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation

    Arguments:
        my_obj (str): object
        filename (str): name of file
    """
    with open(filename, mode="w", encoding="utf-8") as fd:
        fd.truncate(0)
        json.dump(my_obj, fd)

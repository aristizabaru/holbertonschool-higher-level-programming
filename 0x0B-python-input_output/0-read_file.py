#!/usr/bin/python3
"""module 0-read_file

Functions:
    read_file(filename="")
"""


def read_file(filename=""):
    """read to stdout text from a file
    Arguments:
        filename (str): string with file's path
    """
    with open(filename, encoding="utf-8") as fd:
        print(fd.read())

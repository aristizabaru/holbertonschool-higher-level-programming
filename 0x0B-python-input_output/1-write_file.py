#!/usr/bin/python3
"""module 1-write_file

Functions:
    write_file(filename="", text="")
"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8)
    and returns the number of characters written

    Arguments:
        filename (str): string with file's path
        text (str): characters to be written

    Return:
        Number of characters written
    """
    with open(filename, mode="w", encoding="utf-8") as fd:
        return fd.write(text)

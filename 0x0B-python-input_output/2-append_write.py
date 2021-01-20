#!/usr/bin/python3
"""module 2-append_write

Functions:
    append_write(filename="", text="")
"""


def append_write(filename="", text=""):
    """wappends a string at the end of a text file (UTF8) 
    and returns the number of characters added

    Arguments:
        filename (str): string with file's path
        text (str): characters to be written

    Return:
        Number of characters written
    """
    with open(filename, mode="a", encoding="utf-8") as fd:
        open_chars = fd.tell()
        fd.write(text)
        return fd.tell() - open_chars

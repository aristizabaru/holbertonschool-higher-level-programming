#!/usr/bin/python3
"""module 100-append_after

Functions:
    append_after(filename="", search_string="", new_string="")
"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file, after each
    line containing a specific string 

    Arguments:
        filename (str): path and name of file
        search_string (str): string that identify line to skip
        new_string (str): line to insert when line skipped
    """
    lines = list()
    with open(filename, encoding="utf-8", mode="r") as fd:
        for line in fd:
            if search_string in line:
                lines.append(new_string)
            else:
                lines.append(line)
    with open(filename, encoding="utf-8", mode="w") as fd:
        fd.writelines(lines)

#!/usr/bin/python3
"""Module text_indentation

Functions:
    text_indentation(text)
"""


def text_indentation(text):
    """text_indentation()
    prints a text with 2 new lines after each of these characters: ``.`` , ``?`` and ``:``

    Args:
            text (string): sourse text
    Return:
            nothing
    """
    # checks for text
    if type(text) is not str:
        raise TypeError("text must be a string")
    # print new text
    chars = (".", "?", ":")
    no_lines = ""
    lines = text.splitlines()
    for line in lines:
        line = line.strip()
        no_lines += line
    new_lines = ""
    for letter in no_lines:
        new_lines += letter
        if letter in chars:
            new_lines += "\n"
    final_text = ""
    new_lines = new_lines.splitlines()
    for line in new_lines:
        line = line.strip()
        if line[-1] in chars:
            final_text += line + "\n\n"
        else:
            final_text += line
    print(final_text, end="")

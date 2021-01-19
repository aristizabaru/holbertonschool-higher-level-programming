#!/usr/bin/python3
"""Module 10-square

Classes
    Square
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Creates a Rectangle object

    Methods
        __init__(self, size)
    """

    def __init__(self, size):
        """Creates object

        Arguments
            size (int): size value
        """
        super().__init__(size, size)

#!/usr/bin/python3
"""Module 8-rectangle

Classes
    Rectangle
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Creates a Rectangle object

    Methods
        __init__(self, width, height)
    """

    def __init__(self, width, height):
         """Creates object

        Arguments
            width (int): width value
            height (int): height value
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

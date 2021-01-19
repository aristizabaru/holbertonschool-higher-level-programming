#!/usr/bin/python3
"""Module 9-rectangle.py

Classes
    Rectangle
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Creates a Rectangle object

    Methods
        __init__(self, width, height)
        area(self)
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

    def area(self):
        """Calculate an object's area

        Return
            Area of rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """Return printable representation of a Rectangle object
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

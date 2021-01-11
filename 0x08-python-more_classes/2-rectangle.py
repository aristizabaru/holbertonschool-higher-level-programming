#!/usr/bin/python3
"""Module 2-rectangle
"""


class Rectangle:
    """Creates a rectangle object

    Attributes:
        width (int): value representing the width of a square
        height (int): value representing the height of a square

    Methods:
        area(self)
        perimeter(self)
    """

    def __init__(self, width=0, height=0):
        """Constructor of object type Rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Sets width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Sets height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    # Methods
    def area(self):
        """Returns object's area
        """
        return self.__width * self.__height

    def perimeter(self):
        """Returns object's perimeter

        Return:
            Return 0 if height or width are 0
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        width = self.__width * 2
        height = self.__height * 2

        return width + height

#!/usr/bin/python3
"""Module 7-base_geometry

Classes
    BaseGeometry
"""


class BaseGeometry:
    """Creates a BaseGeometry object

    Methods
        area(self)
        integer_validator(self, name, value)
    """

    def area(self):
        """raises an Exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate if `value` is an integer

        Arguments
            name (str): name of object
            value (obj): object to validate
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

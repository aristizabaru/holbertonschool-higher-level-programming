#!/usr/bin/python3
"""MagicClass definition"""
import math


class MagicClass:
    """Represents a MagicClass """

    def __init__(self, radius=0):
        """Initializes the Magic Class"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Calculaes the area of the circle"""
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """Calculates the circumference of the circle"""
        return 2 * math.pi * self.__radius

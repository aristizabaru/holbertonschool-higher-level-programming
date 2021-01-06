#!/usr/bin/python3
"""MagicClass definition"""
import math


class MagicClass:
    """Represents a MagicClass """

    def __init__(self, radius):
        """Initializes the Magic Class"""
        self._MagicClass__radius = 0
        if type(radius) is not int or type(radius) is not float:
            raise TypeError("radius must be a number")
        self._MagicClass__radius = radius

    def area(self):
        """Calculaes the area of the circle"""
        return (self._MagicClass__radius ** 2) * math.pi

    def circumference(self):
        """Calculates the circumference of the circle"""
        return (2 * math.pi) * self._MagicClass__radius

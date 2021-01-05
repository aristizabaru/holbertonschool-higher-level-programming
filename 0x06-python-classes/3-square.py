#!/usr/bin/python3
"""Square class definition"""


class Square:
    """Represents a square

    Attributes:
        __size (int): size of a side of the square
    """

    def __init__(self, size=0):
        """Initializes a square

         Args:
             size (int): size of a side of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """calculates the area of the square.

        Returns:
            The area of the square"""
        return self.__size ** 2

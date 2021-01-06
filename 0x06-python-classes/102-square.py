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
        self.size = size

    @property
    def size(self):
        """getter of __size
        Returns:
            The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setter of __size
        Args:
            value (int): the size of a size of the square
        """
        if not isinstance(value, int) and not isinstance(value, float):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """calculates the current square area

        Returns:
            The area of the square"""
        return self.__size ** 2

    def __eq__(self, other):
        """calculates equality

        Returns:
            True or False"""
        return self.area() == other.area()

    def __ne__(self, other):
        """calculates difference

        Returns:
            True or False"""
        return self.area() != other.area()

    def __gt__(self, other):
        """calculates grater than other

        Returns:
            True or False"""
        return self.area() > other.area()

    def __ge__(self, other):
        """calculates greater or equals to other

        Returns:
            True or False"""
        return self.area() >= other.area()

    def __lt__(self, other):
        """calculates less than other

        Returns:
            True or False"""
        return self.area() < other.area()

    def __le__(self, other):
        """calculates less or equals than other

        Returns:
            True or False"""
        return self.area() <= other.area()

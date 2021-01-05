#!/usr/bin/python3
class Square:
    """
     Square class returns the area given a size

     Args:
        size (int): Representation of size. Size must be >= 0

     Attributes:
        size (int): Representation of size. Size must be >= 0
     """

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """Returns the size of the object"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """calculates the area of the size.

        Returns:
            The area."""
        return self.__size ** 2

    def my_print(self):
        """prints a graphic representation of the area with a '#'"""
        if self.__size == 0:
            print()
        else:
            for row in range(self.__size):
                for hash in range(self.__size):
                    print("#", end="")
                print()

#!/usr/bin/python3
class Square:
    """
     Square class returns the area given a size

     Args:
        size (int): Representation of size. Size must be >= 0

     Attributes:
        size (int): Representation of size. Size must be >= 0
     """

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Returns the position of the object"""
        return self.__position

    @position.setter
    def position(self, value):
        """setter of __position
        Args:
            value (tuple): position of the square in 2D space
        Returns:
            None
        """
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or value[0] < 0 or \
           type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

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
            for row in range(self.__position[1]):
                print()
            for row in range(self.__size):
                for hash in range(self.__position[0]):
                    print(" ", end="")
                for hash in range(self.__size):
                    print("#", end="")
                print()

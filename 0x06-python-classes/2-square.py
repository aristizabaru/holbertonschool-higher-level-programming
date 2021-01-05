#!/usr/bin/python3
class Square:
    """
     Square class handle the `size` field

     Args:
        size (int): Representation of size. Size must be >= 0

     Attributes:
        size (int): Representation of size. Size must be >= 0
     """

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

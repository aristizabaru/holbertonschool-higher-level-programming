#!/usr/bin/python3
"""Module 100-my_int

Classes
    MyInt
"""


class MyInt(int):
    """Creates a MyInt object

    Methods
        __eq__(self, other)
        __ne__(self, other)
    """

    def __eq__(self, other):
        """Extends equality operator
        """
        return int(self) != other

    def __ne__(self, other):
        """Extends inequality operator
        """
        return int(self) == other

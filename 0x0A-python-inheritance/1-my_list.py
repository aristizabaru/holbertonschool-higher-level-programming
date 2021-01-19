#!/usr/bin/python3
"""Module 1-my_list

Class:
    MyList (list)
"""


class MyList(list):
    """Create sorted list object

    Methods:
        print_sorted(self)
    """

    def print_sorted(self):
        """print sorted list
        """
        print(sorted(self))

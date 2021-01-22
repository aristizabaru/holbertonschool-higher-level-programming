#!/usr/bin/python3
"""module 9-student

Class:
    Student
"""


class Student:
    """Creates an intance of Student

    Attributes:
        first_name (str): the first name of the student
        last_name (str): the last name of the student
        age (int): age of the student

    Methods:
        to_json(self)
    """

    def __init__(self, first_name, last_name, age):
        """Constructor
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of a Student instance
        """
        return self.__dict__

#!/usr/bin/python3
"""module 11-student

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

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance
        """
        json_dict = dict()
        is_string = True
        # look if attrs is valid and only has strings
        if attrs is not None:
            for attribute in attrs:
                if type(attribute) is not str:
                    is_string = False
                    break
            if is_string is True:
                for attribute in attrs:
                    if hasattr(self, attribute):
                        json_dict[attribute] = self.__dict__[attribute]
        if attrs is None or is_string is False:
            for attribute in self.__dict__:
                json_dict[attribute] = self.__dict__[attribute]
        return json_dict

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance
        """
        for key in json:
            self.__dict__[key] = json[key]

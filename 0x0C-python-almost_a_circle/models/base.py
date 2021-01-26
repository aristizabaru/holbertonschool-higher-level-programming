#!/usr/bin/python3
"""module base

Class
    Base
"""
import json
import csv
import turtle
import random
import os.path as path


class Base:
    """Manage `id` attribute in all furture instances of this class
    and to avoid duplicating the same code (by extension, same bugs)

    Class Attributes:
        __nb_objects (int): number of instances from Base class

    Methods:
        __init__(self, id=None)

    Class methods:
        create(cls, **dictionary)
        save_to_file(cls, list_objs)
        load_from_file(cls)
        save_to_file_csv(cls, list_objs)
        load_from_file_csv(cls)

    Static methods:
        to_json_string(list_dictionaries)
        from_json_string(json_string)
        draw(list_rectangles, list_squares)
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor

        if `id` is set to `None` the `__nb_objects` is incremented
        by one and set as the id for the new object

        Arguments:
            id (int): id number for the new object
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance of `cls` with all
        attributes already set

        Arguments:
            dictionary (dict): packed key, value arguments
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(width=1, height=1)
        else:
            dummy = cls(size=1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def save_to_file(cls, list_objs):
        """writes Rectangle and Square attributes
        to a JSON file

        Arguments:
            list_objs (list): list of objects
        """
        list_to_json = list()
        # get all objects attributes to list of dictionaries
        if list_objs is not None and len(list_objs) > 0:
            list_to_json = [obj.to_dictionary() for obj in list_objs]
        # serialize to `<Class name>.json` from `list_to_json`
        with open(str(cls.__name__) + ".json", "w", encoding="utf-8") as fd:
            json.dump(list_to_json, fd)

    @classmethod
    def load_from_file(cls):
        """Creates Square or Rectangle objects from
        JSON data set

        Return:
            If file doesn't exist an empty list will
            be returned
        """
        obj_list = list()
        if path.exists(str(cls.__name__) + ".json"):
            with open(str(cls.__name__) + ".json", "r", encoding="utf-8")\
                    as fd:
                # deserialize json
                json_dict = cls.from_json_string(fd.read())
            # unpack every dictionary to `cls.create` to return instances
            obj_list = [cls.create(**obj_d)for obj_d in json_dict]
        return obj_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """writes Rectangle and Square attributes
        to a CSV file

        Arguments:
            list_objs (list): list of objects
        """
        if list_objs is not None and len(list_objs) > 0:
            # get fieldnames from object dictionary data set
            csv_fieldnames = [key for key in list_objs[0]
                              .to_dictionary().keys()]
            # get objects attributes as dictionary data set
            csv__data = [obj.to_dictionary() for obj in list_objs]
        # serialize to `<Class name>.csv` from `csv__data`
        with open(str(cls.__name__) + ".csv", "w", encoding="utf-8") as fd:
            # try to copy data in file, if not posible leave file empty
            try:
                csv_writer = csv.DictWriter(fd, fieldnames=csv_fieldnames)
                csv_writer.writeheader()
                for line in csv__data:
                    csv_writer.writerow(line)
            except Exception:
                pass

    @classmethod
    def load_from_file_csv(cls):
        """Creates Square or Rectangle objects from
        CSV file

        Return:
            If file doesn't exist an empty list will
            be returned
        """
        obj_list = list()
        if path.exists(str(cls.__name__) + ".csv"):
            with open(str(cls.__name__) + ".csv", "r", encoding="utf-8")\
                    as fd:
                # load data into a csv DictReader object
                csv_data = csv.DictReader(fd)
                # get fieldnames length
                keys = len(csv_data.fieldnames)
                # Turn data into a list
                csv_data = list(csv_data)
            # convert every value to its data type
            for obj in csv_data:
                obj["x"] = int(obj["x"])
                obj["y"] = int(obj["y"])
                obj["id"] = int(obj["id"])
                if keys == 5:
                    obj["width"] = int(obj["width"])
                    obj["height"] = int(obj["height"])
                else:
                    obj["size"] = int(obj["size"])
            # unpack every dictionary to `cls.create` to return instances
            obj_list = [cls.create(**obj_d)for obj_d in csv_data]
        return obj_list

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation
        of `list_dictionaries`

        Arguments:
            list_dictionaries (list): list of dictionaries
        """
        list_d = list()
        if list_dictionaries is not None and len(list_dictionaries) > 0:
            list_d = [item for item in list_dictionaries]
        return json.dumps(list_d)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string
        representation `json_string`

        Arguments:
            json_string (str): string representing a list of dictionaries
        """
        json_d = list()
        if json_string is not None and len(json_string) > 0:
            json_d = json.loads(json_string)
        return json_d

    @staticmethod
    def draw(list_rectangles, list_squares=[]):
        """ opens a window and draws all the Rectangles and Squares
        in list_rectangles and list_squares

        Arguments:
            list_rectangles (list): list of Rectangle objects
            list_squares (list): list of Square objects
        """
        # expand list
        to_print = list_rectangles + list_squares
        # config color palette
        bg_fill = ("#D9ECF2", "#F56A79", "#FF414D",
                   "#1AA6B7", "#646BD9")
        bg_stroke = ("#002D40")
        bg_color = ("#F3F6F9")
        # config screen
        my_screen = turtle.Screen()
        my_screen.bgcolor(bg_color)
        # config turtle
        my_turtle = turtle.Turtle()
        my_turtle.hideturtle()
        # check list_rectangles
        if to_print is not None and len(to_print) > 0:
            # draw every rectangle
            for obj in to_print:
                # set x & y position
                my_turtle.setpos(obj.x, obj.y)
                # set stroke and fill color
                my_turtle.color(bg_stroke,
                                bg_fill[random.randint(0, len(bg_fill) - 1)])
                my_turtle.pendown()
                my_turtle.begin_fill()
                # print rectangle
                for i in range(4):
                    if i in [0, 2]:
                        my_turtle.forward(obj.width)
                    else:
                        my_turtle.forward(obj.height)
                    my_turtle.left(90)
                my_turtle.end_fill()
                my_turtle.penup()
        turtle.done()

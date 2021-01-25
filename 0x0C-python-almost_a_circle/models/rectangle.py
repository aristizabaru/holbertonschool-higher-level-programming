#!/usr/bin/python3
"""module rectangle

Class
    Rectangle
"""
from models.base import Base
# Base = __import__("models.base", fromlist=[None]).Base


class Rectangle(Base):
    """Creates a Rectangle object

    Properties:
        width (int): width of the instance
        height (int): height of the instance
        x (int): x coordenate
        y (int): y coordenate
        id (int): object identificator

    Methods:
        __init__(self, width, height, x=0, y=0, id=None)
        def area(self)
        display(self)
        update(self, *args, **kwargs)
        def to_dictionary(self)

    Magic Methods:
        __str__(self)
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor

        Id parameter is set by the superclass `Base`

        Arguments:
            width (int): width of the instance
            height (int): height of the instance
            x (int): x coordenate
            y (int): y coordenate
            id (int): object identificator
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    # properties
    @property
    def width(self):
        """return width"""
        return self.__width

    @property
    def height(self):
        """return height"""
        return self.__height

    @property
    def x(self):
        """return x"""
        return self.__x

    @property
    def y(self):
        """return y"""
        return self.__y

    # setters
    @width.setter
    def width(self, value):
        """sets width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """sets height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """sets x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """sets y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    # Methods
    def area(self):
        """return area of the instance"""
        return self.width * self.height

    def display(self):
        """print to stdout the graphic representation
        of the object taking x and y as reference
        to the position of the object in the screen
        """
        print("\n"*self.y, end="")
        for i in range(self.height):
            print(" "*self.x, end="")
            print("#"*self.width)

    def update(self, *args, **kwargs):
        """Update the object's attributes

        Arguments
            args (int): packed list, the order of arguments
            must be as follow:
            - 1st argument should be the id attribute
            - 2nd argument should be the width attribute
            - 3rd argument should be the height attribute
            - 4th argument should be the x attribute
            - 5th argument should be the y attribute

            kwargs(int): packed key, value pair. if `*args`
            is not available then `*kwargs`will be assigned
        """
        if args is not None and len(args) > 0:
            attributes = ["id", "width", "height", "x", "y"]
            for idx, value in enumerate(args):
                if idx < 5 and hasattr(self, attributes[idx]):
                    setattr(self, attributes[idx], value)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """ Returns the dictionary representation
        of the object
        """
        return {"x": self.x, "y": self.y, "id": self.id,
                "height": self.height, "width": self.width}

    # Magic methods
    def __str__(self):
        """overriding the __str__ method so that it returns
        `[Rectangle] (<id>) <x>/<y> - <width>/<height>`
        """
        return "[Rectangle] ({}) {}/{} - {}/{}"\
            .format(self.id, self.x, self.y, self.width, self.height)

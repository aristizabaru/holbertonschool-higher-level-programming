#!/usr/bin/python3
"""module square

Class
    Square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Creates a Square object

    Properties:
        size (int): represent width and height
        from Rectangle class
        x (int): x coordenate
        y (int): y coordenate
        id (int): object identificator

    Methods:
        __init__(self, size, x=0, y=0, id=None)
        def update(self, *args, **kwargs)
        def to_dictionary(self)

    Magic Methods:
        __str__(self)
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor

        All parameters are set by the parent class Rectangle

        Arguments:
            size (int): represent width and height
            x (int): x coordenate
            y (int): y coordenate
            id (int): object identificator
        """
        super().__init__(self.size, self.size, x, y, id)

    # properties
    @property
    def size(self):
        """return size"""
        return self.width

    # setters
    @size.setter
    def size(self, value):
        """sets size"""
        self.width = value
        self.height = value

    # methods
    def update(self, *args, **kwargs):
        """Update the object's attributes

        Arguments
            args (int): packed list, the order of arguments
            must be as follow:
            - 1st argument should be the id attribute
            - 2nd argument should be the size attribute
            - 4th argument should be the x attribute
            - 5th argument should be the y attribute

            kwargs(int): packed key, value pair. if `*args`
            is not available then `*kwargs`will be assigned
        """
        if args is not None and len(args) > 0:
            attributes = ["id", "size", "x", "y"]
            for idx, value in enumerate(args):
                if idx < 4 and hasattr(self, attributes[idx]):
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
                "size": self.size}

    # Magic methods
    def __str__(self):
        """overriding the __str__ method so that it returns
        `[Square] (<id>) <x>/<y> - <size>`
        """
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.size)

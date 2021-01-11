#!/usr/bin/python3
"""Module 9-rectangle
"""


class Rectangle:
    """Creates a rectangle object

    Class attributes:
        number_of_instances (int): number of instances the
                                   class Rectangle has initializated
         print_symbol (object): used as symbol for string representation. It
                                has to be an iterable object

    Attributes:
        width (int): value representing the width of a square
        height (int): value representing the height of a square

    Methods:
        area(self) : Returns object's area
        perimeter(self): Returns object's perimeter

    Magic Methods:
        __str__(self): Returns object's printable representation
        __repr__(self): Returns object's representation
        __del__(self): Prints message before object's destruction

    Class Methods:
        square(cls, size=0): Create a new Rectangle instance

    Static Methods:
        bigger_or_equal(rect_1, rect_2): Returns the biggest rectangle
                                         based on the area
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Constructor of object type Rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieve width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Sets width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Sets height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    # Methods
    def area(self):
        """Returns object's area
        """
        return self.__width * self.__height

    def perimeter(self):
        """Returns object's perimeter

        Return:
            Return 0 if height or width are 0
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        width = self.__width * 2
        height = self.__height * 2

        return width + height

    # Magic methods
    def __str__(self):
        """Returns object's printable representation

        The __str__ method prints the object's area
        using # to stdout

        Return:
            Return empty string if height or width are 0
        """
        r_string = ""
        if self.__width == 0 or self.__height == 0:
            return r_string
        for row in range(self.__height):
            r_string += "\n"
            for col in range(self.__width):
                r_string += str(self.print_symbol)
        return r_string[1:]

    def __repr__(self):
        """Returns object's representation

        This method makes possible to recreate an object
        with the sames attributes using eval()

        Return:
            Return string representation of the object that
            can be recreated using eval()
        """
        if self.__width == 0 or self.__height == 0:
            return "Rectangle()"
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Prints message before object's destruction
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    # Class methods
    @classmethod
    def square(cls, size=0):
        """Create a new Rectangle instance

        Arguments
            size (int): present width and height of the new instance

        Return
            Rectangle object
        """
        return cls(size, size)

    # Statactic methods
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area

        Arguments
            rect_1 (Rectangle): Rectangle object
            rect_2 (Rectangle): Rectangle object

        Return
            Rectangle object with the biggest area
            If both rectangles have equal area 'rect_1' is returned
        """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        result = rect_1
        if rect_1.area() < rect_2.area():
            result = rect_2
        return result

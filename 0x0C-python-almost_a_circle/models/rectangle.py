#!/usr/bin/python3

from models.base import Base

class Rectangle(Base):
    """A rectangle class representation"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """A new Rectangle initialization

        Args:
	    height : The height of the new Rectangle
            width : The width of the new Rectangle
            x : The x coordinate of the new Rectangle
	    id : The identity of the new Rectangle
            y : The y coordinate of the new Rectangle
        Errors:
            TypeError: If the width or the height is not an integer
            ValueError: If width or height is equal or less than 0
            TypeError: If  x or y is not an integer
            ValueError: If the parameter x or y is less than 0
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def width(self):
        """the function to set or get the width of the Rectangle"""
        return self.__width

    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    def height(self):
        """the function to set or get the height of the Rectangle"""
        return self.__height

    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    def x(self):
        """the function to set or get the x rectangle coordinate"""
        return self.__x

    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value
    def y(self):
        """the function to set or get the y rectangle coordinate"""
        return self.__y

    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """The function to return the area of the Rectangle"""
        return self.width * self.height

    def display(self):
        """The function to print the area of the rectangle using the `#`"""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def update(self, *args, **kwargs):
        """The function to update the Rectangle

        Args:
            #args : the value of the new attribute
                - The parameter id attribute
                - The parameter width attribute
                - The parameter height attribute
                - The parameter x attribute
                - The parameter y attribute
            ##kwargs: New key or value pairs of attributes
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """the function defines for a rectangle the dictionary representation"""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """The functiion returns the print() and str() for a Rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)

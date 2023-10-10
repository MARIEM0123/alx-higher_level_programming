#!/usr/bin/python3
"""the Rectangle class definition"""


class Rectangle:
    """the rectangle representation"""

    def __init__(self, width=0, height=0):
        """Initialisation to a new Rectangle.

        Args:
            width: The width of the new rectangle.
            height: The height of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """definition of the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """the function to have the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ the function to get the area of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """the function to get the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

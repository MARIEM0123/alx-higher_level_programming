#!/usr/bin/python3
"""The class Rectangle inherited from BaseGeometry definition"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """The BaseGeometry rectangle definition"""

    def __init__(self, width, height):
        """A new Rectangle initialization

        Args:
            width : The new Rectangle width
            height : The new Rectangle height
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

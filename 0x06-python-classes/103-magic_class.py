#!/usr/bin/python3
"""Define a MagicClass """

import math

class MagicClass:
    """The circle"""

    def __init__(self, radius=0):
        """Initialization

        Arg:
            radius: The radius of the MagicClass.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """set the area"""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Return The circumference"""
        return (2 * math.pi * self.__radius)

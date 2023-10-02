#!/usr/bin/python3
"""The class Square"""

class Square:
    """The square OF THE CLASS"""

    def __init__(self, size=0):
        """Initialization OF THE CLASS

        Args:
            size: The size of the class
        """
        self.size = size

    @property
    def size(self):
        """Get the size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)

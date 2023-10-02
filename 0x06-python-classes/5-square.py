#!/usr/bin/python3
"""The class Square."""

class Square:
    """The square of the class"""

    def __init__(self, size):
        """Initialization to the class

        Args:
            size The size of the class
        """
        self.size = size

    @property
    def size(self):
        """Get size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """The return for area"""
        return (self.__size * self.__size)

    def my_print(self):
        """THE RETURN for my_print"""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")

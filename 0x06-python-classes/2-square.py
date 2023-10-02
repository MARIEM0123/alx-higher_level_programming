#!/usr/bin/python3
""" the class Square."""

class Square:
    """the square"""

    def __init__(self, size=0):
        """Initialization

        Args:
            size: The size
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

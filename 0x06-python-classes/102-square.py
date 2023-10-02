#!/usr/bin/python3
"""the class Square"""

class Square:
    """the square FOR the class"""

    def __init__(self, size=0):
        """Initialization to the class

        Args:
            size (int): The size of the class
        """
        self.size = size

    @property
    def size(self):
        """Set the size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area"""
        return (self.__size * self.__size)

    def __eq__(self, other):
        """return the equal comparision to a Square"""
        return self.area() == other.area()

    def __ne__(self, other):
        """Define the difference to a Square."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Define the less than a Square."""
        return self.area() < other.area()

    def __le__(self, other):
        """Define the less or equal to a Square."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Define the higher than a Square."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Define the higher or equal to  a Square."""
        return self.area() >= other.area()

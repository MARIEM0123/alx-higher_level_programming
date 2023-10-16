#!/usr/bin/python3
from models.rectangle import Rectangle

class Square(Rectangle):
    """The representation of a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """ A new Square initialization

        Args:
            size: The size parameter
	    id: The identity parameter
            x: The x coordinate parameter
            y: The y coordinate parameter
        """
        super().__init__(size, size, x, y, id)

    def size(self):
        """The size to get or set the size of the new square."""
        return self.width

    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """The function to update the Square

        Args:
            -args (ints): New attribute values
                - Argument parameter
                - Argument parameter
                - Argument parameter of the x attribute
                - Argument parameter of the y attribute
            -kwargs (dict): New key or  value pairs of attributes
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """The function defines the dictionary representation of the Square"""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """The function defines the  print() and str() of a Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

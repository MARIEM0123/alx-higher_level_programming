#!/usr/bin/python3
"""The base geometry class BaseGeometry definition"""


class BaseGeometry:
    """the class is representing the base geometry."""

    def area(self):
        """if not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Check if a parameter is an integer.

        Args:
            name : The name of the parameter
            value (int): The parameter for validation
        Raises:
            TypeError: If value is not an integer
            ValueError: If value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

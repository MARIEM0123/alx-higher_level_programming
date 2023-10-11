#!/usr/bin/python3
"""An inherited class-checking function definition"""


def inherits_from(obj, a_class):
    """Checks if an object is an inherited instance of a class

    Args:
        obj: The object to check if is an inherited of a class
        a_class : The class to check of the type of object
    Returns:
        True if the object is an inherited instance of a_class
        False Otherwise
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False

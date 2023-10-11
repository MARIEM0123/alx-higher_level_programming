#!/usr/bin/python3
"""A class-checking function definition"""

def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a given class

    Args:
        obj : A given object
        a_class : The class for the type of object
    Returns:
        True or False depending to the case
    """
    if type(obj) == a_class:
        return True
    return False

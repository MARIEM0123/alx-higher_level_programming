#!/usr/bin/python3
"""A class checking function definition"""

def is_kind_of_class(obj, a_class):
    """Check if an object is an instance or inherited instance of a class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        True if an object is an instance or inherited instance of a_class
        False Otherwise
    """
    if isinstance(obj, a_class):
        return True
    return False

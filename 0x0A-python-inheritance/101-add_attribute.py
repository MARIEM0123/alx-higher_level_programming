#!/usr/bin/python3
"""The function to add attributes to objects definition"""


def add_attribute(obj, att, value):
    """Add a new attribute to an object if possible

    Args:
        obj : The given object
        att : The name of the attribute to add to object
        value : The value of attribute
    Raises:
        TypeError: If the attribute can't be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)

#!/usr/bin/python3

"""A name-printing function definition"""

def say_my_name(first_name, last_name=""):
    """to get the  name

    Args:
        first_name: The first name to get
        last_name: The last name to get
    Raises:
        TypeError: One of the parameters is not string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))

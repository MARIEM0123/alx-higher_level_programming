#!/usr/bin/python3

def safe_print_integer(value):
    """ the function prints "{:d}".format().

    Args:
        value: The integer

    Returns:
        Booleen
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)

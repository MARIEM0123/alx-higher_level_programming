#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    """To execute a function

    Args:
        fct: The function
        args: Arguments

    Returns:
        deoends to the case the result or None if error
    """
    try:
        x = fct(*args)
        return (x)
    except:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)

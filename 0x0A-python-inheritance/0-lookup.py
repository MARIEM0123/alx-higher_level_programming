#!/usr/bin/python3
"""the object attribute lookup function definiiotn"""


def lookup(obj):
    """list of an object's available attributes is the return """
    return (dir(obj))

#!/usr/bin/python3
"""The class-to-JSON function definition"""

def class_to_json(obj):
    """The output the dictionary representation of a simple data structure."""
    return obj.__dict__

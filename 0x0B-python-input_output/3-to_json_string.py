#!/usr/bin/python3
"""the function defines a string-to-JSON"""
import json

def to_json_string(my_obj):
    """the output is the JSON representation of a string object"""
    return json.dumps(my_obj)

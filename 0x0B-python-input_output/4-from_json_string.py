#!/usr/bin/python3
"""the JSON-to-object function definition"""
import json

def from_json_string(my_str):
    """the output is object representation of a JSON string."""
    return json.loads(my_str)

#!/usr/bin/python3
"""The function to create a JSON file"""
import json

def load_from_json_file(filename):
    """from a JSON to create a Python object"""
    with open(filename) as f:
        return json.load(f)

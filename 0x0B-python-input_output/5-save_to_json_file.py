#!/usr/bin/python3
import json

def save_to_json_file(my_obj, filename):
    """Using the JSON representation to write an object"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)

#!/usr/bin/python3
"""A text file insertion function definition"""

def append_after(filename="", search_string="", new_string=""):
    """take a given string in a file and insert txt at the start of the line

    Args:
        filename : The filename
        search_string : The string to search for within the file
        new_string (str): The string to insert
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text

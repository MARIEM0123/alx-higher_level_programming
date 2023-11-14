#!/usr/bin/python3
"""writing to a file function definition"""

def write_file(filename="", text=""):
    """the function writes a string to a text file

    Args:
        filename: The file name
        text: The text to wrote to the file
    Returns:
        The number of chars in the string
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)

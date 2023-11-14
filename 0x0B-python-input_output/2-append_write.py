#!/usr/bin/python3
"""appending a string to the file function definition"""

def append_write(filename="", text=""):
    """Appends a string to the text file

    Args:
        filename: The filename
        text: The string to append to the file
    Returns:
        The number of characters to append to the end of the file
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)

#!/usr/bin/python3
"""Text file-reading function definition"""

def read_file(filename=""):
    """get the contents of the text file to stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")

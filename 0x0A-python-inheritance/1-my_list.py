#!/usr/bin/python3
"""the inherited list class MyList definiiotn"""


class MyList(list):
    """Write a class MyList that inherits from list"""

    def print_sorted(self):
        """Print a list in sorted ascending order."""
        print(sorted(self))

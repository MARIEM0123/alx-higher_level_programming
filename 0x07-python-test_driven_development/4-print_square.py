#!/usr/bin/python3

"""Square-printing function definition"""

def print_square(size):
    """return the square with the # character

    Args:
        size: The height or width of the square
    Raises:
        TypeError: If size =! interger
        ValueError: If size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")

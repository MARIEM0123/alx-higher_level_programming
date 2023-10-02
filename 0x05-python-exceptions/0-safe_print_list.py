#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Print x elememts of a list.

    Args:
        my_list: The listof elements
        x (int): The elemnts number

    Returns:
        there is a return
    """
    y = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            y += 1
        except IndexError:
            break
    print("")
    return (y)

#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """the function prints the x elemnts in a list

    Args:
        my_list: The given list
        x : The elements number type integer

    Returns:
        there is a return
    """
    y = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            y += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (y)

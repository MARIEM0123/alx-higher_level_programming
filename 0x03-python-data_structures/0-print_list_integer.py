#!/usr/bin/python3i

def print_list_integer(my_list=[]):
    """The function prints the integers of a list."""
    for i in range(len(my_list)):
        print("{:d}".format(my_list[i]))

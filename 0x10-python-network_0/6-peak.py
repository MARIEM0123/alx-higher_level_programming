#!/usr/bin/python3
"""The Module to find a peak between integers"""


def find_peak(list_of_integers):
    """The function to find a peak between unsorted integers.

    Args:
        list_of_integers (list): this is the list

    You are allowed to make an algorithm with the the lowest complexity.


    The first method check every single element and find out if it is qualified
    as a peak. This solutionhas the complexity of O(n) time or O(1)

    Returns:
        int: peak(s)
    """
    list_ = list_of_integers
    # if the list doens't exist  return None
    if list_ == []:
        return None
    length = len(list_)

    start, end = 0, length - 1
    while start < end:
        mid = start + (end - start) // 2
        if list_[mid] > list_[mid - 1] and list_[mid] > list_[mid + 1]:
            return list_[mid]
        if list_[mid - 1] > list_[mid + 1]:
            end = mid
        else:
            start = mid + 1
    return list_[start]

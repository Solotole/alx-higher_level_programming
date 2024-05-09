#!/usr/bin/python3
""" script finding peak in an unsorted list """


def find_peak(list_of_integers):
    """ function finding peak
    Args:
        list_of_integers (list): list of unsorted list
    """
    list_copy = list_of_integers
    if not list_copy
        return None
    length = len(list_copy)

    start, end = 0, length - 1
    while start < end:
        mid = start + (end - start) // 2
        if list_copy[mid] > list_copy[mid - 1] and list_copy[mid] > list_copy[mid + 1]:
            return list_copy[mid]
        if list_copy[mid - 1] > list_copy[mid + 1]:
            end = mid
        else:
            start = mid + 1
    return list_[start]

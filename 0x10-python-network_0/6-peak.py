#!/usr/bin/python3
""" script finding peak in an unsorted list """


def max_value(list_l):
    """ function to find maximum value
    Args:
        list_l (list): finding maximum value in a list
    """
    if list_l[0] > list_l[1]:
        return list_l[0]
    elif list[0] < list_l[1]:
        return list_l[1]
    else:
        return list_l[0]


def find_peak(list_of_integers):
    """ function finding peak
    Args:
        list_of_integers (list): list of unsorted list
    """
    list_l = list_of_integers
    length = len(list_l)
    mid = int(length / 2)
    if list_l == []:
        return None
    if length == 1:
        return list_l[0]
    if length == 2:
        return max_val(list_l)
    if list_l[mid] > list_l[mid - 1] and \
            list_l[mid] < list_l[mid + 1]:
        return list_l[mid]
    if list_l[mid] > list_l[mid + 1]:
        return find_peak(list_l[mid + 1:])
    if list_l[mid] < list_l[mid - 1]:
        return find_peak(list_l[:mid])

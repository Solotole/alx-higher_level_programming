#!/usr/bin/python3
"""Pascal Triangle"""


def pascal_triangle(n):
    """print Pascal Triangle

    n (int): size of Pascal's Triangle

    Returns:
        return list of list of integers
    """
    list1 = []
    list2 = []
    list3 = []
    value = 0
    if n <= 0:
        return []
    else:
        for i in range(n + 1):
            for j in range(i):
                if j == 0:
                    list1.append(1)
                elif j + 1 == i:
                    list1.append(1)
                    break
                else:
                    value = list3[j - 1] + list3[j]
                    list1.append(value)
            list3 = list1
            list1 = []
            if len(list3) != 0:
                list2.append(list3)
        return list2

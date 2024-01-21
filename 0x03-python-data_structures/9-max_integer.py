#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    else:
        max_var = my_list[0]
        length = len(my_list)
        for i in range(1, length, 1):
            if max_var < my_list[i]:
                max_var = my_list[i]
            else:
                continue
    return max_var

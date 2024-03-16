#!/usr/bin/python3
def element_at(my_list, idx):
    value = 0
    if not my_list:
        if idx < 0:
            return None
        elif idx >= len(my_list):
            return None
        else:
            value = my_list[idx]
    return my_list[idx]

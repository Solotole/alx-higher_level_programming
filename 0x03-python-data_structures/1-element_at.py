#!/usr/bin/python3
def element_at(my_list, idx):
    if not my_list:
        if idx < 0:
            return None
        if idx >= len(my_list):
            return None
    return my_list[idx]

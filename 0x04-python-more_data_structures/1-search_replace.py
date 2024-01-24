#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    if my_list != []:
        new_list = my_list[:]
        for i in range(0, len(my_list), 1):
            if my_list[i] == search:
                new_list[i] = replace
            else:
                continue
    else:
        new_list = my_list[:]
    return new_list

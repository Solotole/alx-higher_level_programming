#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = {}
    if a_dictionary != {}:
        # new_dict = a_dictionary.copy()
        for i in a_dictionary:
            new_dict[i] = a_dictionary[i] * 2
    else:
        new_dict = a_dictionary.copy()
    return new_dict

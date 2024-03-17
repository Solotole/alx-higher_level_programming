#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    n_list = []
    if a_dictionary and value is not None:
        for key, data in a_dictionary.items():
            n_list.append(key)
            n_list.append(data)
        if n_list.count(value) == 0:
            return a_dictionary
        elif n_list.count(value) > 0:
            for nums in range(1, len(n_list), 2):
                if n_list[nums] == value:
                    del a_dictionary[n_list[nums - 1]]
            return a_dictionary
    else:
        return None

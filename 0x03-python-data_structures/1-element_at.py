#!usr/bin/python3
def element_at(my_list, idx):
    value = 0
    if idx < 0:
        value = 'None'
    elif idx > len(my_list) - 1:
        value = 'None'
    else:
        value = my_list[idx]
    return value

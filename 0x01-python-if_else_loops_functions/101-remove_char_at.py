#!/usr/bin/python3
def remove_char_at(str, n):
    string = ""
    size = len(str)
    for i in range(size):
        if i != n:
            string += str[i]
        else:
            continue
    return string

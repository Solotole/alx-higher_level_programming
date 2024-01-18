#!/usr/bin/python3
def remove_char_at(str, n):
    list = []
    size = len(str)
    for i in range(size):
        if i != n:
            list = str[i]
    print("{0:s}".format(list))

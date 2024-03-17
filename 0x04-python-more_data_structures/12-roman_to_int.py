#!/usr/bin/python3
"""module Roman literal to integer
"""


def roman_to_int(roman_string):
    summation = 0
    loops = 0
    new_dict = {}
    new_dict = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
    if roman_string is None or type(roman_string) != str:
        return 0
    elif roman_string is not None and type(roman_string) == str:
        for i in range(len(roman_string)):
            for j in new_dict.keys():
                if j == roman_string[i]:
                    if summation < new_dict[j] and loops > 0:
                        summation = new_dict[j] - summation
                    else:
                        summation += new_dict[j]
                else:
                    continue
                loops += 1
        return summation

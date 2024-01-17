#!/usr/bin/python3
def last_digit(number):
    print("{0:d}".format(number))

for i in range(0, 100, 1):
    if i < 99:
        print("{0:0>2d}".format(i), end=", ")
    elif i == 99:
        last_digit(i)
    else:
        pass

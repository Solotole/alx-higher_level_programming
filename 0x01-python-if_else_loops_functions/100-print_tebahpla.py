#!/usr/bin/python3
def confirm(value):
    if value % 2 == 0:
        return True
    if value % 2 != 0:
        return False


def reverse_alternating():
    for i in range(122, 96, -1):
        print("{:c}".format(i if confirm(i) else i - 32), end="")


reverse_alternating()

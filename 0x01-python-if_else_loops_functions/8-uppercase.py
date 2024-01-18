#!/usr/bin/python3
def determinant(s):
    if s >= 97 and s <= 122:
        return True
    if s < 97 or s > 122:
        return False


def uppercase(str):
    size = len(str)
    for i in range(size):
        string = ord(str[i])
        if (string >= 97 and string <= 122) or (string < 97 or string > 122):
            if i != (size - 1):
                print("{:c}".format(string - 32 
                    if determinant(string) else string), end="")
            if i == (size - 1):
                print("{0:c}".format(string - 32))
        else:
            pass

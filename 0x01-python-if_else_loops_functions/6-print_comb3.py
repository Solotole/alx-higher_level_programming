#!/usr/bin/python3
for a in range(0, 10, 1):
    for b in range(0, 10, 1):
        if a < b and a != b:
            if a != 8 or b != 9:
                print("{0:d}{1:d}".format(a, b), end=", ")
            elif a == 8 and b == 9:
                print("{0:d}{1:d}".format(a, b))
        else:
            pass
    else:
        continue

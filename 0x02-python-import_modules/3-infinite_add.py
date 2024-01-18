#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    sum = 0
    args_count = len(argv)
    for i in range(1, args_count, 1):
        sum += int(argv[i])
    print("{}".format(sum))

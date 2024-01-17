#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
value = int(number / 10)
value2 = number - (value * 10)
if value2 > 5:
    print("Last digit of {0:d}i is {1:d} and is greater than 5".format(number, value2))
elif value2 == 0:
    print("Last digit of {0:d} is {1:d} and is 0".format(number, value2))
elif value2 < 6 and value2 != 0:
    print("Last digit of {0:d} is {1:d} and is less than 6 and not 0".format(number, value2))

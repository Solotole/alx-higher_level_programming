#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if str(number)[-1] == 'i':
    number = number[0:-1]
    number = int(number)
else:
    pass

if number < 0:
    value2 = number % -10
else:
    value2 = number % 10
string1 = "Last digit of {0:d}i is {1:d} and is greater than 5"
string2 = "Last digit of {0:d} is {1:d} and is less than 6 and not 0"
if value2 > 5:
    print(string1.format(number, value2))
elif value2 == 0:
    print("Last digit of {0:d} is {1:d} and is 0".format(number, value2))
elif value2 < 6 and value2 != 0:
    print(string2.format(number, value2))

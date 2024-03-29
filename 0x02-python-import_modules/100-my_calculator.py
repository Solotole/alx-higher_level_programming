#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    length = len(argv)
    if length != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    c = argv[2]
    b = int(argv[3])
    if c == '+':
        addition = add(a, b)
        print(f"{a} {c} {b} = {addition}")
    elif c == "-":
        subtraction = sub(a, b)
        print(f"{a} {c} {b} = {subtraction}")
    elif c == "*":
        multiplication = mul(a, b)
        print(f"{a} {c} {b} = {multiplication}")
    elif c == "/":
        division = div(a, b)
        print(f"{a} {c} {b} = {division}")
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

#!/usr/bin/python3
def safe_print_division(a, b):
    value = 0
    try:
        value = a / b
        return value
    except (ZeroDivisionError):
        value = None
        return None
    finally:
        print("Inside result: {:}".format(value))

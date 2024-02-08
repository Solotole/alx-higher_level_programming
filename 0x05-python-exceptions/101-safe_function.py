#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    result = 0
    try:
        if args != None:
            result = fct(args[0], args[1])
        return result
    except (TypeError, ValueError, IndexError, ZeroDivisionError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return None

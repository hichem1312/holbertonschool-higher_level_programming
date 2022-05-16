#!/usr/bin/python3
def safe_print_integer(value):
    x = 0
    try:
        x += value
        print("{:d}".format(value))
        return True
    except TypeError:
        return False
    except ValueError:
        return False

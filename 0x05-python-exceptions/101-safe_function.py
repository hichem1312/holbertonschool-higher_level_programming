#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        a = fct(*args)
        return a
    except Exception as ex:
        print("Exception: {}".format(ex), file=sys.stderr)
        return None

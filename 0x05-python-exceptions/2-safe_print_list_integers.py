#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    j = 0
    i = 0
    while i < x:
        try:
            print("{:d}".format(my_list[i]), end="")
            i += 1
            j += 1
        except TypeError:
            i += 1
        except ValueError:
            i += 1
    print()
    return(j)

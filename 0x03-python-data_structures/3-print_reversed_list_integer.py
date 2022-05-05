#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for i in reversed(range(len(my_list))):
        if i == len(my_list) - 1:
            print("{:d}".format(my_list[i]))
        else:
            print("{:d}".format(my_list[i]))

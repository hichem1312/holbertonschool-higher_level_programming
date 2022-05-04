#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        print("None")
        exit(1)
    elif idx >= len(my_list):
        print("None")
        exit(1)
    else:
        for i in range(len(my_list)):
            if i == idx:
                print("Element at index {:d} is {:d}".format(i, my_list[i]))
                exit(1)

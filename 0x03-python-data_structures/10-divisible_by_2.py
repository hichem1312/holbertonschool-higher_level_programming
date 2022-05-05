#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    cmpp = [None] * len(my_list)
    for i in range(0, len(my_list)):
        if my_list[i] % 2 == 0:
            cmpp[i] = True
        else:
            cmpp[i] = False
    return cmpp

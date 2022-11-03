#!/usr/bin/python3
def weight_average(my_list=[]):
    x = 0
    tu_ple = 0
    if len(my_list) == 0:
        return 0
    for tuple in my_list:
        x += tuple[1]
        tu_ple += (tuple[0] * tuple[1])
    res = tu_ple / x
    return res

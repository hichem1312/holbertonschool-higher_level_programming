#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if (my_list[idx] < 0):
        return(my_list)
    elif (idx in range(0, len(my_list))):
        my_list[idx] = element
        return(my_list)
    else:
        return(my_list)

#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    f = 0
    for i in sorted(a_dictionary):
        if i == key:
            a_dictionary[i] = value
            f = 1
    if f == 0:
        a_dictionary[key] = value
    return(a_dictionary)

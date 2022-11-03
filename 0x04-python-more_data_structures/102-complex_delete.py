#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for i in (a_dictionary):
        if i == value:
            del i
    return a_dictionary

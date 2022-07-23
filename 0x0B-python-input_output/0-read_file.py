#!/usr/bin/python3
'''method'''


def read_file(filename=""):
    '''define'''
    with open(filename, "r", encoding="UTF-8") as file:
        print(file.read(), end="")

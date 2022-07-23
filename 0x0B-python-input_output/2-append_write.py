#!/usr/bin/python3
'''methode'''


def append_write(filename="", text=""):
    '''define'''
    with open(filename, "a", encoding="UTF-8") as file:
        file.write(text)
        return len(text)

#!/usr/bin/python3
'''methode'''


def write_file(filename="", text=""):
    '''define'''
    with open(filename, "w", encoding="UTF-8") as file:
        file.write(text)
        return len(text)

#!/usr/bin/python3
"""square"""


def print_square(size):
    """function"""

    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    ch = ""
    if size == 0:
        return
    for i in range(0, size):
        for j in range(0, size):
            ch += '#'
        ch += "\n"
    ch = ch[0:len(ch) - 1]
    print(ch)

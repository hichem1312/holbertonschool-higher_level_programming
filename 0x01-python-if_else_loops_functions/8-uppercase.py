#!/usr/bin/python3
def uppercase(str):
    n_string = ""
    for i in (str):
        if ord((i)) >= 97 and ord((i)) <= 123:
            n_string += chr(ord(i) - 32)
        else:
            n_string += i
    print("{:s}".format(n_string), end="")
    print("")

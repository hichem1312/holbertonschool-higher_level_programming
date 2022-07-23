#!/usr/bin/python3
'''importation'''


import json


def save_to_json_file(my_obj, filename):
    '''define'''
    j = json.dumps(my_obj)
    with open(filename, "a", encoding="UTF-8") as file:
        file.write(j)

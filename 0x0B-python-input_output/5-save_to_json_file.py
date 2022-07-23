#!/usr/bin/python3
'''importation'''


import json


def save_to_json_file(my_obj, filename):
    '''define'''
    with  open(filename, mode="w+") as f:
         json.dump(my_obj, f)

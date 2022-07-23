#!/usr/bin/python3
"""importation"""
import json


def load_from_json_file(filename):
    """define"""
    with open(filename, mode="r") as f:
        return json.load(f)

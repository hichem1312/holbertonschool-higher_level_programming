#!/usr/bin/python3
""" fetching https://intranet.hbtn.io/status"""
import requests

if __name__ == '__main__':
    req = requests.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type:", type(req.text))
    print("\t- content:", req.text)

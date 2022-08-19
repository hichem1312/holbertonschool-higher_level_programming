#!/usr/bin/python3
""" sends a post request to the passed URL"""


from urllib import request, parse
from sys import argv

if __name__ == '__main__':
    data = bytes(parse.urlencode(
        {"email": argv[2]}).encode('utf-8'))
    with request.urlopen(argv[1], data=data) as html:
        print(html.read().decode('utf-8'))

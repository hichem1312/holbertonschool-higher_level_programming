#!/usr/bin/python3
""" send a request to the URL and displays the value"""


from sys import argv
from urllib.request import urlopen

if __name__ == '__main__':
    with urlopen(argv[1]) as url:
        print(url.headers["X-Request-Id"])

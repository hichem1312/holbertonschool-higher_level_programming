#!/usr/bin/python3
"""fetches URL"""
from urllib.request import urlopen

if __name__ == '__main__':
    with urlopen('https://intranet.hbtn.io/status') as response:
        d = response.read()
        print('Body response:')
        print('\t- type: {}'.format(type(d)))
        print('\t- content: {}'.format(d))
        print('\t- utf8 content: {}'.format(d.decode('utf-8')))

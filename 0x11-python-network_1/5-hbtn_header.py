#!/usr/bin/python3
"""takes in a URL, sends a request to the URL
and displays the value of the
variable X-Request-Id"""
from requests import get
from sys import argv


if __name__ == '__main__':
    url = argv[1]
    response = get(url)
    info = response.
    print(info.get('X-Request-Id'))

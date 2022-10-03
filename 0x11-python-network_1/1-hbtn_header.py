#!/usr/bin/python3
"""Fetches a URL while using urllib package
with a 'with' statement"""

from urllib.request import urlopen
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    with urlopen(url) as response:
        info = response.info()
        print(info['X-Request-Id'])

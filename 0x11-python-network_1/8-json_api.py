#!/usr/bin/python3
"""akes in a URL and an email, sends a POST request to the
passed URL with the email as a parameter
and displays the body of the response (decoded in utf-8)"""

from requests import post, codes
from sys import argv

if __name__ == "__main__":

    url = 'http://0.0.0.0:5000/search_user'

    if len(argv) > 1:
        q = {'q': argv[1]}
    else:
        q = {'q': ''}
    response = post(url, data=q)
    try:
        obj = response.json()
        if len(obj) == 0:
            print('No result')
        else:
            print('[{}] {}'.format(obj['id'], obj['name']))
    except(ValueError):
        print('Not a valid JSON')

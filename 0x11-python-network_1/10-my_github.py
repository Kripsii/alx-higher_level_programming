#!/usr/bin/python3

"""takes your GitHub credentials
(username and password)
and uses the GitHub API to display your id"""

from requests import get
from sys import argv
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    url = 'https://api.github.com/user'
    username = argv[1]
    password = argv[2]
    response = get(url, auth=HTTPBasicAuth(username, password))
    try:
        obj = response.json()
        print(obj.get('id'))
    except ValueError:
        print(None)
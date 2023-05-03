#!/usr/bin/python3
"""
    This script takes my Github credentials(username and password) and
    uses the GitHub API to display the id
"""


import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    url = 'https://api.github.com/user'

    r = requests.get(url, auth=HTTPBasicAuth(sys.argv[1], sys.argv[2]))

    print(r.json().get('id'))

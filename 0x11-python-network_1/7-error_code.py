#!/usr/bin/python3
"""
    This script takes in a URL, sends a request to the URL and displays
    the body of the response.
    If the status code is greater than/equal to 400, print Error Code:
    followed by the value of the HTTP status code.
    You are only allowed to use requests and sys packages
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    req = requests.get(url)
    if req.status_code >= 400:
        print(f"Error code: {req.status_code}")
    else:
        print(req.text)

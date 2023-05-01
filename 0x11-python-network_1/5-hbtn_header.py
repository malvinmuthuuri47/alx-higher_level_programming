#!/usr/bin/python3
"""
    This script takes a URL, sends a request to that URL and displays
    the value of the variable provided in the response header
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)
    print(response.headers.get("X-Request-Id"))

#!/usr/bin/python3
import requests
import sys
"""
    This script takes a URL, sends a request to that URL and displays
    the value of the variable provided in the response header
"""

if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    print(response.headers["X-Request-Id"])

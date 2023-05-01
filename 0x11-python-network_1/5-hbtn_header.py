#!/usr/bin/python3
"""
    This script takes a URL, sends a request to that URL and displays
    the value of the variable provided in the response header
"""
import sys
import requests


response = requests.get(sys.argv[1])
print(response.headers["X-Request-Id"])

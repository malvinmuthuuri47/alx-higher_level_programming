#!/usr/bin/python3
"""
Script sends a request to a URL and displays the value of
the dictionary key passed to it using the method GET.
"""

import urllib.request
import sys

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.headers.get("X-Request-Id"))

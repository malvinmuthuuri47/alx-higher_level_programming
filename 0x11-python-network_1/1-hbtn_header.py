#!/usr/bin/python3
"""
Script sends a request to a URL and displays the value of
the dictionary key passed to it using the method GET.
"""

import urllib.request
if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        print(response.headers.get("X-Request-Id"))

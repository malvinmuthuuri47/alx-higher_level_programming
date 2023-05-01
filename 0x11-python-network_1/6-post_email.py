#!/usr/bin/python3
import sys
import requests
"""
    This script takes in a URL and an email address, sends a POST request
    to the passed URL with the email as a parameter and finally displays
    the body of the response
"""


if __name__ == "__main__":
    url = sys.argv[1]
    myData = {'email': sys.argv[2]}

    response = requests.post(url, data=myData)
    print(response.text)
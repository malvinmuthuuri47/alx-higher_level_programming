#!/usr/bin/python3
"""
    This script takes in a letter and sends a POST request to the given URL
    with the letter as a parameter.
    You need to check if command-line arguments are supplied other than the
    file name and if the server response if in a valid JSON format.
"""
import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) == 1:
        myData = {'q': ''}
    else:
        myData = {'q': sys.argv[1]}

    url = 'http://0.0.0.0:5000/search_user'
    req = requests.post(url, data=myData)

    try:
        req = req.json()
        if req == {}:
            print("No result")
        else:
            print(f"[{req.get('id')}] {req.get('name')}")

    except ValueError:
        print("Not a valid JSON")

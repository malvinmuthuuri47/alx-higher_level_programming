#!/usr/bin/python3
import requests
"""This script fetches from a URL using the package requests"""


response = requests.get("https://alx-intranet.hbtn.io/status")
print("Body response:")
print(f"\t- type: {type(response.text)}")
print(f"\t- content: {response.text}")

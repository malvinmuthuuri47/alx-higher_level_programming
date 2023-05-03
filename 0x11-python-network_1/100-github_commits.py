#!/usr/bin/python3
"""
    This script lists the commits made in github.
"""


import sys
import requests

if __name__ == "__main__":
    url = f'https://api.github.com/repos/{sys.argv[2]}/{sys.argv[1]}/commits'

    r = requests.get(url)
    commits = r.json()

    for commit in commits[:10]:
        sha = commit.get("sha")
        authors = commit["commit"]["author"]["name"]
        print(f"{sha}: {authors}")

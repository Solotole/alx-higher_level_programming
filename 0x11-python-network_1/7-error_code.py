#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL and displays
the body of the response.

Usage: ./7-error_code.py <URL>
  - Handles HTTP errors.
"""


if __name__ == "__main__":
    import requests
    from sys import argv
    url = argv[1]
    req = requests.get(url)

    if req.status_code >= 400:
        print("Error code: {}".format(req.status_code))
    else:
        print(req.text)

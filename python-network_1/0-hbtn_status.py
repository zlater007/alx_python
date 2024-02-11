#!/usr/bin/python3
"""A script that
- uses the requests package
"""
import requests

"""
- fetches https://alx-intranet.hbtn.io/status.
"""
if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'
    response = requests.get(url)

    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))
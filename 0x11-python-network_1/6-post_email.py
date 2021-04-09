#!/usr/bin/python3
"""0-hbtn_status module"""
import requests
import sys


def main(req, data):
    """handles http request and print response"""
    response = requests.post(req, data=data)
    print(response.text)


if __name__ == "__main__":
    # config
    if len(sys.argv) > 2:
        url = sys.argv[1]
        data = {'email': sys.argv[2]}
        # init
        main(url, data)

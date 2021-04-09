#!/usr/bin/python3
"""0-hbtn_status module"""
import requests
import sys


def main(req):
    """handles http request and print response"""
    response = requests.get(req)
    print(response.headers.get("X-Request-Id"))


if __name__ == "__main__":
    # config
    if len(sys.argv) > 1:
        url = sys.argv[1]
        # init
        main(url)

#!/usr/bin/python3
"""0-hbtn_status module"""
from urllib import request
import sys


def main(req):
    """handles http request and print response"""
    with request.urlopen(req) as response:
        header = response.getheader("X-Request-Id")
        print(header)


if __name__ == "__main__":
    # config
    if len(sys.argv) > 1:
        url = sys.argv[1]
        req = request.Request(url)
        # init
        main(url)

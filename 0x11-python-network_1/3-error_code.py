#!/usr/bin/python3
"""0-hbtn_status module"""
from urllib import request, parse, error
import sys


def main(req):
    """handles http request and print response"""
    try:
        with request.urlopen(req) as response:
            print(response.read().decode())
    except error.URLError as err:
        print("Error code: {}".format(err.code))


if __name__ == "__main__":
    # config
    if len(sys.argv) > 1:
        url = sys.argv[1]
        req = request.Request(url)
        # init
        main(req)

#!/usr/bin/python3
"""0-hbtn_status module"""
import requests


def main(req):
    """handles http request and print response"""
    with requests.get(req) as response:
        print("Body response:\n\t- type: {}\n\t- content: "
              "{}".format(type(response.text), response.text))


if __name__ == "__main__":
    # config
    url = "https://intranet.hbtn.io/status"
    # init
    main(url)

#!/usr/bin/python3
"""0-hbtn_status module"""
import requests
import sys


def main(credentials):
    """handles http request and print response"""
    session = requests.Session()
    session = session.get("https://api.github.com/user", auth=(credentials))
    if session.status_code == requests.codes.ok:
        json_data = session.json()
        print(json_data['id'])
    session.close()


if __name__ == "__main__":
    # config
    credentials = (sys.argv[1], sys.argv[2])
    # init
    main(credentials)

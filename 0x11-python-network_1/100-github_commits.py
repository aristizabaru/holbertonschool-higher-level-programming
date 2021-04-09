#!/usr/bin/python3
"""0-hbtn_status module"""
import requests
import sys
import json


def main(url):
    """handles http request and print response"""
    session = requests.Session()
    session = session.get(url)
    if session.status_code == requests.codes.ok:
        json_data = session.json()
        for i, obj in enumerate(json_data):
            if i == 10:
                break
            print("{}: {}".format(obj['sha'],
                                  obj['commit']['author']['name']))
    session.close()


if __name__ == "__main__":
    # config
    repository_name = sys.argv[1]
    owner_name = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(owner_name,
                                                              repository_name)
    # init
    main(url)

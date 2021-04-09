#!/usr/bin/python3
"""0-hbtn_status module"""
import requests
import sys


def main(req, data):
    """handles http request and print response"""
    response = requests.post(req, data=data)
    try:
        json_data = response.json()
        if len(json_data) == 0:
            print("No result")
        else:
            print("[{}] {}".format(json_data['id'], json_data['name']))
    except Exception:
        print("Not a valid JSON")


if __name__ == "__main__":
    # config
    if len(sys.argv) > 1:
        data = {'q': sys.argv[1]}
    else:
        data = {'q': ''}
    url = "http://0.0.0.0:5000/search_user"
    # init
    main(url, data)

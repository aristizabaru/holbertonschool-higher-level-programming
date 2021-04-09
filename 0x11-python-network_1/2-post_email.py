# #!/usr/bin/python3
"""0-hbtn_status module"""
from urllib import request, parse 
import sys


def main(req):
    """handles http request and print response"""
    with request.urlopen(req) as response:
        content = response.read().decode()
        print(content)


if __name__ == "__main__":
    # config
    if len(sys.argv) > 2:
        url = sys.argv[1]
        values = {'email': sys.argv[2]}
        data = parse.urlencode(values)
        data = data.encode('ascii') # data should be bytes
        req = request.Request(url, data)
        # init
        main(req)

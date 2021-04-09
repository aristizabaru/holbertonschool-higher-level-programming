# #!/usr/bin/python3
"""0-hbtn_status module"""
from urllib import request


def main(req):
    """handles http request and print response"""
    with request.urlopen(req) as response:
        content = response.read()
        content_decoded = content.decode()
        print("Body response:\n\t- type: {}\n\t- content: "
              "{}\n\t- utf8 content: {}".format(type(content), content, content_decoded))


if __name__ == "__main__":
    # config
    url = "https://intranet.hbtn.io/status"
    req = request.Request(url)
    # init
    main(req)

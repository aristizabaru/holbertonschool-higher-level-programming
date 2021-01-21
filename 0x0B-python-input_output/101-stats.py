#!/usr/bin/python3
"""module 101-stats

Reads stdin line by line and computes metrics
"""
import sys


# config
lines = 1
file_size = 0
status_codes = dict()
# print line
try:
    for data in sys.stdin:
        data = data.rstrip()
        # find file size
        start_idx = data.rfind(" ") + 1
        # check if value is digit
        if data[start_idx:].isdigit() is False:
            continue
        file_size += int(data[start_idx:])
        # find status codes
        code = data[start_idx - 4: start_idx - 1]
        # check if value is digit
        if code.isdigit() is False:
            continue
        # count status codes
        if code in status_codes:
            status_codes[code] += 1
        else:
            status_codes[code] = 1
        if lines % 10 == 0:
            print("File size: {}".format(file_size))
            sort_codes = sorted(status_codes.items())
            for key, value in sort_codes:
                print("{}: {}".format(key, value))
        lines += 1
    # if program ends print
    print("File size: {}".format(file_size))
    sort_codes = sorted(status_codes.items())
    for key, value in sort_codes:
        print("{}: {}".format(key, value))
except KeyboardInterrupt:
    print("File size: {}".format(file_size))
    sort_codes = sorted(status_codes.items())
    for key, value in sort_codes:
        print("{}: {}".format(key, value))

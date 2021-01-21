#!/usr/bin/python3
"""module 101-stats

Reads stdin line by line and computes metrics
"""

# config
lines = 1
file_size = 0
status_codes = dict()
# print line
try:
    while True:
        data = input()
        # find file size
        start_idx = data.rfind(" ") + 1
        file_size += int(data[start_idx:])
        # find status codes
        code = data[start_idx - 4: start_idx]
        # count status codes
        if code in status_codes:
            status_codes[code] += 1
        else:
            status_codes[code] = 1
        if lines % 10 == 0:
            print("File size: {}".format(file_size))
            sort_codes = sorted(status_codes.items())
            status_codes.clear()
            for key, value in sort_codes:
                print("{}: {}".format(key, value))
        lines += 1
except KeyboardInterrupt:
    print("File size: {}".format(file_size))
    for key in status_codes:
        print("{}: {}".format(key, status_codes[key]))

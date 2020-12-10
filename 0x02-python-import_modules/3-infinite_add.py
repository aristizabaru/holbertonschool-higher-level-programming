#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    result = 0
    for index in range(len(argv)):
        if index is not 0:
            result += int(argv[index])
    print(result)

#!/usr/bin/python3
for char in reversed(range(ord("a"), ord("z")+1)):
    print("{}".format(chr(char).upper() if not char %
                      2 == 0 else chr(char).lower()), end="")

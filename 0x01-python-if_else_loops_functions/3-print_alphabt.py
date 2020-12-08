#!/usr/bin/python3
for character in range(ord("a"), ord("z")+1):
    if character is not(ord("e")) and character is not(ord("q")):
        print("{:c}".format(character), end="")

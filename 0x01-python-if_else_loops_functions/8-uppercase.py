#!/usr/bin/python3
def uppercase(str):
    new_char = ""
    for char in str:
        if char >= "a" and char <= "z":
            new_char = ord(char) - 32
        else:
            new_char = ord(char)
        print("{:c}".format(new_char), end="")
    print("")

#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary:
        new_list = sorted(a_dictionary.items())
        for item in new_list:
            print("{}: {}".format(item[0], item[1]))

#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    if set_1 and set_2:
        new_list = set_1 ^ set_2
        return new_list
    else:
        return None

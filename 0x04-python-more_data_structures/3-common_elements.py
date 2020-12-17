#!/usr/bin/python3
def common_elements(set_1, set_2):
    if set_1 and set_2:
        new_list = set_1 & set_2
        return new_list
    elif set_1:
        return set_1
    elif set_2:
        return set_2
    else:
        return None

#!/usr/bin/python3
def complex_delete(my_dict, value):
    duplicate = my_dict.copy()
    for key, val in duplicate.items():
        if value in val:
            del my_dict[key]
    return my_dict

#!/usr/bin/python3
def complex_delete(my_dict, value):
    erase = []
    for key in my_dict:
        if str(my_dict[key]) in value:
            erase.append(key)
    for key in erase:
        del my_dict[key]

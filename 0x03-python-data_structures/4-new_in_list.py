#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < len(my_list) and idx > -1:
        new_list = my_list[:]
        new_list[idx] = element
        return new_list
    else:
        return my_list

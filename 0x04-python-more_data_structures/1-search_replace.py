#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list:
        new_list = []
        for idx, item in enumerate(my_list):
            if item == search:
                new_list.append(replace)
            else:
                new_list.append(item)
        return new_list
    else:
        return my_list

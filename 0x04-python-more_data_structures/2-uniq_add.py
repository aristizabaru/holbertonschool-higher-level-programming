#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    if my_list:
        my_list.sort()
        for i, num in enumerate(my_list):
            if i < len(my_list) - 1 and num != my_list[i+1]:
                result += num
            elif i == len(my_list)-1 and num != my_list[i-1]:
                result += num
    return result

#!/usr/bin/python3
def uniq_add(list=[]):
    prev_n = 0
    result = 0
    if list:
        list.sort()
        for num in list:
            if num != prev_n:
                result += num
                prev_n = num
    return result

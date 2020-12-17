#!/usr/bin/python3
def weight_average(my_list=[]):
    result = 0
    mul = 0
    add = 0
    if my_list:
        for item in my_list:
            temp = item[0] * item[1]
            add += item[1]
            mul += temp
        result = mul / add
    return result

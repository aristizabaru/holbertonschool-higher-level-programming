#!/usr/bin/python3
"""module 12-pascal_triangle

Class:
    Student
"""


def pascal_triangle(n):
    """returns a list of lists of integers representing
    the Pascal’s triangle of n

    Arguments:
        n (int): number of rows

    Return:
        list representing pascal's triangle values
    """
    pascal = list()
    if n <= 0:
        return pascal

    for i in range(n):
        temp_list = list()
        for j in range(i + 1):
            if j == 0 or j == i:
                temp_list.append(1)
            else:
                temp_list.append(pascal[i-1][j-1] + pascal[i-1][j])
        pascal.append(temp_list)
    return pascal

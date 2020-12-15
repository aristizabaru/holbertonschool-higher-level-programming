#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for idx, element in enumerate(row):
            if idx is not len(row)-1:
                print("{} ".format(element), end="")
            else:
                print("{}".format(element))

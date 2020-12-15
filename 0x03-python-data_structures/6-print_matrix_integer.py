#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for row in matrix:
            for idx, element in enumerate(row):
                print("{:d}".format(element), end="")
                if idx is not len(row) - 1:
                    print(" ", end="")
            print("")

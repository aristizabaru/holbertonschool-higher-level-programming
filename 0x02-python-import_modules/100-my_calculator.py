#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    operators = ["+", "-", "*", "/"]
    if len(argv) is not 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a, b, op = argv[1], argv[3], argv[2]
    if op in operators:
        if op is operators[0]:
            print("{} {} {} = {:d}".format(a, op, b, add(int(a), int(b))))
        elif op is operators[1]:
            print("{} {} {} = {:d}".format(a, op, b, sub(int(a), int(b))))
        elif op is operators[2]:
            print("{} {} {} = {:d}".format(a, op, b, mul(int(a), int(b))))
        elif op is operators[3]:
            print("{} {} {} = {:d}".format(a, op, b, div(int(a), int(b))))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

signo = ""
if number < 0:
    signo = "-"
if abs(number) % 10 is 0:
    print("Last digit of {} is {} {}".format(
        number,  abs(number) % 10, "and is zero"))
elif abs(number) % 10 > 5 and number > 0:
    print("Last digit of {} is {}{} {}".format(
        number, signo, abs(number) % 10, "and is greater than 5"))
else:
    print("Last digit of {} is {}{} {}".format(
        number, signo, abs(number) % 10, "and is less than 6 and not 0"))

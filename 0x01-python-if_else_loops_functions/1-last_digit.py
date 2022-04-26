#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    a = -number
else:
    a = number
b = a % 10
if b == 0:
    print("last digit of {:d} is 0 and is 0".format(number))
elif b < 6 or number < 0:
    print ("last digit of {:d} is {:} and is less than 6 and not 0".format(number,int(b * (number / a))))
elif b > 5:
    print("last digit of {:d} is {:d} and is greater than 5".format(number, b))

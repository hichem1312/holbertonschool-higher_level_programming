#!/usr/bin/python3
import random
n = random.randint(-10000, 10000)
x = abs(n) % 10
if n < 0:
    x = -x
print("Last digit of {} is {} and is ".format(n, x), end="")
if x > 5:
    print("greater than 5")
elif x == 0:
    print("0")
else:
    print("less than 6 and not 0")

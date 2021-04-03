from itertools import count
from math import factorial


def my_factorial():
    for el in count(1):
        yield factorial(el)


my_gener = my_factorial()
x = 0
for i in my_gener:
    if x < 15:
        print(i)
        x += 1
    else:
        break
from itertools import cycle
from sys import argv

my_funcs, arg_1, arg_2, arg_3 = argv


my_list = [arg_1, arg_2, arg_3]


def my_funcs(my_list):
    i = 0
    for el in cycle(my_list):
        if i > 10:
            break
        else:
            print(el)
            i += 1
    return


print(my_funcs(my_list))


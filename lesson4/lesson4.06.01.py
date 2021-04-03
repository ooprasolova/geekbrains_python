from sys import argv
from itertools import count

script_name, arg_1, arg_2 = argv

arg_1 = int(arg_1)
arg_2 = int(arg_2)


def my_funcs(arg_1, arg_2):
    for el in count(arg_1):
        if el > arg_2:
            break
        else:
            print(el)
    return


print(my_funcs(arg_1, arg_2))







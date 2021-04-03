from functools import reduce
my_list = reduce(lambda x, y: x * y, [el for el in list(range(100, 1001)) if el%2 == 0])
print(my_list)
class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        for i in range(len(self.my_list)):
            for j in range(len(self.my_list[i])):
                print(self.my_list[i][j], end=' ')
            print()
        return ''

    def __add__(self, other):
        result = [[self.my_list[i][j] + other.my_list[i][j] for j in range(len(self.my_list[0]))] for i in range(len(other.my_list))]
        return result


my_list = Matrix([[31, 22, 5], [37, 43, 12], [51, 86, 45]])
my_list2 = Matrix([[3, 5, 6], [2, 4, 5], [5, 64, 8]])
print(my_list)
print(my_list2)
print(Matrix(my_list.__add__(my_list2)))


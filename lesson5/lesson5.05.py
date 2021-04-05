"""  5. Создать (программно) текстовый файл,
записать в него программно набор чисел,
разделенных пробелами. Программа должна подсчитывать
 сумму чисел в файле и выводить ее на экран."""

result = []
my_list = input("Введите строку чисел: ")
my_list = my_list.split()
for string in my_list:
    for component in string.split():
        result.append(int(component))
        summa = sum(result)
with open("lesson5.05.txt", "w") as f:
    for i in my_list[:]:
        f.write(f'{i}\n')


print(summa)



# print(pay)
#
# def my_func():
#     summa = 0
#     print("Для остановки введите #")
#     while True:
#         result = [summa]
#         my_list = input("Введите строку чисел: ")
#         my_list = my_list.split()
#         for string in my_list:
#             for component in string.split():
#                 result.append(int(component))
#                 summa = sum(result)
#             try:
#                 component = '#'
#             except ValueError:
#                 print("Это не число")
#                 return summa
#             else:
#                 continue
#         print(summa)
#
#
# print(my_func())
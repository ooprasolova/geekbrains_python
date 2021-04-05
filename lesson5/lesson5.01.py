"""1. Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка."""


my_list = []
while True:
    i = input("Введите данные: ")
    my_list.append(i)
    if not i:
        break
with open("lesson5.01.txt", "w") as f:
    for i in my_list[:-1]:
        f.write(f'{i}\n')
    f.write(my_list[-1])

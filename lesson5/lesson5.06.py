"""6. Необходимо создать (не программно) текстовый файл,
где каждая строка описывает учебный предмет и наличие лекционных,
 практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета
и общее количество занятий по нему. Вывести словарь на экран."""

with open('lesson5.06.txt', encoding='utf-8') as file:
    lines = file.read().splitlines()

academic_plan = {}
for line in lines:
    key, value = line.split(':')
    academic_plan.update({key: {value}})
    academic_plan[key] = (value)
for name in academic_plan.keys():
    a = academic_plan[name]
    word_list = a.split()
    num_list = []
    for word in word_list:
        if word.isnumeric():
            num_list.append(int(word))
            study_hors = (sum(num_list))
    print(f'{name}: {study_hors}')
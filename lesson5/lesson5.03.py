"""  3. Создать текстовый файл (не программно),
построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников."""

with open('lesson5.03.txt', encoding='utf-8') as file:
    lines = file.read().splitlines()

staff = {}

for line in lines:
    key, value = line.split(' ')
    staff.update({key:value})
    staff[key] = int(value)

losers_staff = {}
for key, value in staff.items():
    if value < 20000:
        losers_staff[key] = value

print(f'Зарплата меньше 20000 у: ', list(losers_staff.keys()))

pay = 0
for value in staff.values():
    pay += value
    i = len(staff)
    average_pay = pay // i

print(f"Средняя зарплата: ", average_pay)


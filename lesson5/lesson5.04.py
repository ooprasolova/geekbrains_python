"""  4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
 Новый блок строк должен записываться в новый текстовый файл."""

baz = {}
baz_rus = ['Один', 'Два', 'Три', 'Четыре']
with open('lesson5.04.txt', encoding='utf-8') as file:
    lines = file.read().splitlines()
for line in lines:
    key, value = line.split(' — ')
    baz.update({key:value})
    baz[key] = int(value)
    baz_f = dict(zip(baz_rus, list(baz.values())))
with open('lesson5.04.new.txt', 'w') as f:
    for key, value in baz_f.items():
        f.write(f'{key} — {value}\n')
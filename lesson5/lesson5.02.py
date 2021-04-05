"""2. Создать текстовый файл (не программно),
 сохранить в нем несколько строк, выполнить подсчет
 количества строк, количества слов в каждой строке."""

lines = 0
for line in open('lesson5.02.txt', 'r'):
    lines += 1
print("Всего строк:", lines)

for word in open('lesson5.02.txt', 'r'):
    for char in '.,':
        word = word.replace(char, '')
        word_list = word.split()
    print(f"Слов строке:", len(word_list))
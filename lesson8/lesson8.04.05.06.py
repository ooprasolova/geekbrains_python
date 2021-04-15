class Equipment:

    def __init__(self, name, price, art, number_of_lists, *args):
        self.name = name
        self.price = price
        self.art = art
        self.numb = number_of_lists
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {'Наименование': self.name, 'Модель': self.price, 'Артикул': self.art}

    def __str__(self):
        return f'{self.name} цена {self.price} артикул {self.art}'

    def reception(self):

        while True:
            try:
                name = input(f'Введите наименование ')
                mood = int(input(f'Введите модель '))
                art = int(input(f'Введите артикул '))
                unique = {'Наименование': name, 'Модель': mood, 'Артикул': art}
                self.my_unit.update(unique)
                self.my_store.append(self.my_unit)
                print(f'Список -\n {self.my_store}')
            except:
                print(f'Ошибка')
                print(f'Для выхода - x, продолжение - y')
                next = input()
                if next == 'y':
                    self.my_store_full.append(self.my_store)

                elif next == 'x':
                    print(f'Список: \n {self.my_store_full}')
                    return f'Выход'
            break


class Printer(Equipment):
    color = 'red'

    def __init__(self, color):
        self.color = color

    def __str__(self):
        return print(f'Зона погрузки \n {self.color}')


class Scanner(Equipment):
    color = 'blue'

    def __init__(self, color):
        self.color = color

    def __str__(self):
        return print(f'Зона погрузки \n {self.color}')


class Copier(Equipment):
    color = 'green'

    def __init__(self, color):
        self.color = color

    def __str__(self):
        return print(f'Зона погрузки \n {self.color}')


unit_1 = Printer('HP')
unit_2 = Scanner('Cannon')
unit_3 = Copier('LG')
print(unit_1.reception())
print(unit_2.reception())
print(unit_3.reception())





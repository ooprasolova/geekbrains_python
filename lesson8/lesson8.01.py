class MyData:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        my_list = []

        for i in day_month_year.split():
            if i != '':
                my_list.append(i)

        return int(my_list[0]), int(my_list[1]), int(my_list[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 3000 >= year >= 0:
                    return f'Все верно'
                else:
                    return f'Неправильный год'
            else:
                return f'Неправильный месяц'
        else:
            return f'Неправильный день'

    def __str__(self):
        return f'Текущая дата {MyData.extract(self.day_month_year)}'


today = MyData('25 9 2001')
print(today)
print(MyData.valid(13, 16, 2022))
print(today.valid(42, 12, 2011))
print(MyData.extract('11 11 2011'))
print(today.extract('22 12 2006'))
print(MyData.valid(26, 10, 2008))
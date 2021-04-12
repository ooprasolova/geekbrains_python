class Clothes:
    count_clothes = 0


    def __add__(self, other):
        self.s = (self.square_c + self.square_j) * Clothes.count_clothes

    def __str__(self):
        return print(f'Общий расход ткани {self.s}')


class Coat(Clothes):

    def __init__(self, v):
        v = v
        self.square_c = round(v / 6.5 + 0.5)
        Clothes.count_clothes += 1

    def __str__(self):
        return f'Расход ткани на пальто {self.square_c} метра'


class Jacket(Clothes):

    def __init__(self, h):
        h = h
        self.square_j = round(h * 2 + 0.3)
        Clothes.count_clothes += 1

    def __str__(self):
        return f'Расход ткани на костюм {self.square_j} метра'


coat = Coat(46)
jacket = Jacket(1.78)
summa = Clothes
print(coat)
print(jacket)
print(summa)




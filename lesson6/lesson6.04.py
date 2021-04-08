class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} поехала'

    def stop(self):
        return f'{self.name} остановилась'

    def turn_right(self):
        return f'{self.name} повернула на право'

    def turn_left(self):
        return f'{self.name} повернула на лево'

    def show_speed(self):
        return f'Скорость {self.name} сейчас {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Скорость машины {self.name} в городе {self.speed}')

        if self.speed > 40:
            return f'Скорость {self.name} составляет {self.speed}, скорость выше разрешенной'
        else:
            return f'Скорость {self.name} составляет {self.speed}, скорость не выше разрешенной'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость машины {self.name} составляет {self.speed}')

        if self.speed > 60:
            return f'Скорость {self.name} выше разрешенной'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} это полиция'
        else:
            return f'{self.name} это не полиция'


honda = SportCar(50, 'Black', 'Honda', False)
nissan = TownCar(150, 'White', 'Nissan', False)
toyota = WorkCar(70, 'Green', 'Toyota', True)
lexus = PoliceCar(200, 'Blue',  'Lexus', True)
print(honda.turn_left())
print(f'когда {toyota.turn_right()}, {nissan.turn_left()}, {honda.stop()}, a {lexus.show_speed()}')
print(f'Тогда {nissan.go()} и {toyota.turn_left()},а {nissan.show_speed()}')
print(f'{lexus.name} {lexus.color}')
print(f'{nissan.name} это полицейская машина? {nissan.is_police}')
print(f'{lexus.name} это полицейская машина? {lexus.is_police}')
print(honda.show_speed())
print(toyota.show_speed())
print(lexus.police())
print(lexus.show_speed())

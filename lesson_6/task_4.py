class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} начал движение'

    def stop(self):
        return f'{self.name} остановилась'

    def turn_right(self):
        return f'{self.name} повернул направо'

    def turn_left(self):
        return f'{self.name} повернул налево'

    def show_speed(self):
        return f'Текущая скорость {self.name} составляет {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость town car {self.name} составляет {self.speed}')

        if self.speed > 40:
            return f'Скорость {self.name} превышает максимально доступную для town car'
        else:
            return f'Нормальна скорость для {self.name} составляет  town car'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость work car {self.name} составляет {self.speed}')

        if self.speed > 60:
            return f'Скорость {self.name} превышает максимально доступную для work car'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} из полицейского департамента'
        else:
            return f'{self.name} не из полицейского департамента'


bmw = SportCar(100, 'Белая', 'БМВ', False)
mers = TownCar(30, 'Черный', 'Мерседес', False)
sitr = WorkCar(70, 'Желтый', 'Ситроен', True)
ham = PoliceCar(110, 'Оранжевый', 'Хамер', True)
print(sitr.turn_left())
print(f'Когда {mers.turn_right()}, тогда {bmw.stop()}')
print(f'{ham.go()} со скоростью {ham.show_speed()}')
print(f'{sitr.name}  {sitr.color}')
print(f'А {bmw.name} полицейская машина? {bmw.is_police}')
print(f'А {sitr.name} полицейская машина? {sitr.is_police}')
print(bmw.show_speed())
print(mers.show_speed())
print(ham.police())
print(ham.show_speed())

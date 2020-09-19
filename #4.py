class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self, speed=0):
        self.speed += speed
        if self.speed == 0:
            self.speed = int(input('Введите скорость: '))
        print(f'Машина поехала со скоростью {self.speed}')

    def stop(self):
        print('Машина остановилась')
        self.speed = 0

    def turn(self, direction):
        print(f'Машина повернула в направлении {direction}')

    def show_speed(self):
        print(f'Текущая скорость {self.speed}')


class TownCar(Car):
    def show_speed(self):
        print(f'Текущая скорость {self.speed}')
        if self.speed > 60:
            print('Скорость превышена!')


class WorkCar(Car):
    def show_speed(self):
        print(f'Текущая скорость {self.speed}')
        if self.speed > 40:
            print('Скорость превышена!')


class SportCar(Car):
    pass


class PoliceCar(Car):
    is_police = True


TownCar1 = TownCar(61, 'black', 'Tree')
TownCar1.go(10)
TownCar1.show_speed()
print(TownCar1.is_police)
print(TownCar1.color)
TownCar1.stop()
TownCar1.go(30)
TownCar1.show_speed()

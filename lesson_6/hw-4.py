import random


class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed, self.color, self.name, self.is_police = speed, color, name, is_police

    def go(self):
        print(f'Автомобиль {self.name} поехал')

    def stop(self):
        print(f'Автомобиль {self.name} остановился')

    def turn(self):
        direction = ['направо', 'налево']
        print(f'Автомобиль {self.name} повернул {direction[random.randint(0, 1)]}')

    def show_speed(self):
        print(f'Автомобиль {self.name} движется со скоростью {self.speed} км/ч'
              if self.is_police is True or self.speed <= 80 else f'Автомобиль {self.name} превышает скорость')


class TownCar(Car):

    def show_speed(self):
        print(f'Автомобиль {self.name} движется со скоростью {self.speed}'
              if self.speed <= 60 else f'Автомобиль {self.name} превышает скорость')


class SportCar(Car):

    def turbo_mode(self):
        print(f'Автомобиль {self.name} аактивирол турбо режим')
        self.speed *= 1.1


class WorkCar(Car):

    def show_speed(self):
        print(f'Автомобиль {self.name} движется со скоростью {self.speed}'
              if self.speed <= 40 else f'Автомобиль {self.name} превышает скорость')


class PoliceCar(Car):

    def to_chase_mode(self, boost):
        self.speed += boost
        print(f'Автомобиль {self.name} увеличил скорость на {boost} км/ч и включил\033[31m красный\033[0m маячок')


police_car = PoliceCar(150, 'blue', 'Chevrolet', True)
town_car = TownCar(100, 'white', 'Mazda', False)
work_car = WorkCar(20, 'yellow', 'Ford', False)
sport_car = SportCar(200, 'red', 'Mercedes', False)

police_car.show_speed()
work_car.show_speed()
town_car.show_speed()
police_car.to_chase_mode(23)

print(police_car.speed)
print(police_car.name)
print(police_car.color)
print(police_car.is_police)

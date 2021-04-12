"""
4. Реализуйте базовый класс Car.
у класса должны быть следующие атрибуты: speed, color, name, is_police(булево). А также методы: go, stop,
turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Вызовите
методы и покажите результат.
"""


class Car():

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False
        # Введение ещё одного атрибута для хранения состояния подвижности автомобиля
        self._going = False

    def go(self):
        if not self._going:
            print(f'Машина с названием {self.name} поехала!')
            self._going = True

    def stop(self):
        if self._going:
            print(f'Машина с названием {self.name} остановилась!')
            self._going = False

    def turn(self, direction):
        if self._going:
            print(f'Машина с названием {self.name} повернула {direction}!')

    def show_speed(self):
        print(f'Машина с названием {self.name} имеет скорость {self.speed if self._going else 0}!')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('Превышение скорости')
        else:
            print(f'Машина с названием {self.name} имеет скорость {self.speed if self._going else 0}!')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('Превышение скорости')
        else:
            print(f'Машина с названием {self.name} имеет скорость {self.speed if self._going else 0}!')


class PoliceCar(Car):
    # Переопределение конструктора, чтобы назначить is_police
    def __init__(self, *args):
        super().__init__(*args)
        self.is_police = True


town = TownCar(50, 'black', 'town')
sport = SportCar(100, 'red', 'sport')
work = WorkCar(50, 'green', 'work')
police = PoliceCar(100, 'blue', 'police')
print(town.is_police)
town.go()
town.turn('направо')
work.show_speed()
police.show_speed()
police.go()
police.show_speed()

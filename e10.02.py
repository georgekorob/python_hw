"""
2.	Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная сущность (класс)
этого проекта — одежда, которая может иметь определённое название. К типам одежды в этом проекте
относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Выполнить общий подсчёт расхода ткани. Проверить на практике полученные на этом уроке знания.
Реализовать абстрактные классы для основных классов проекта и проверить работу декоратора @property.
"""
from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def __init__(self, name, size):
        pass

    @abstractmethod
    def costs(self):
        pass


class Coat(Clothes):
    def __init__(self, name, size):
        self.name = name
        self.V = size

    @property
    def costs(self):
        return self.V / 6.5 + 0.5


class Costume(Clothes):
    def __init__(self, name, size):
        self.name = name
        self.H = size

    @property
    def costs(self):
        return 2 * self.H + 0.3


coat = Coat('coat', 8)
costume = Costume('costume', 10)
print(costume.costs + coat.costs)

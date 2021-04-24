"""
4.	Начать работу над проектом «Склад оргтехники». Создать класс, описывающий склад. А также класс «Оргтехника», 
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). 
В базовом классе определить параметры, общие для приведённых типов. В классах-наследниках реализовать параметры, 
уникальные для каждого типа оргтехники.

5.	Продолжить работу над предыдущим заданием. Разработать методы, которые отвечают за приём оргтехники на склад и
передачу в определённое подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру (например, словарь).

6.	Продолжить работу над предыдущим заданием. Реализовать механизм валидации вводимых пользователем данных. Например,
для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
"""
from abc import ABC, abstractmethod
from enum import Enum


class Equipment(ABC):
    class Type(Enum):
        Printer = 0
        Scanner = 1
        Xerox = 2

    ids = 0

    def __init__(self, name: str):
        self.id = Equipment.ids
        Equipment.ids += 1
        self.__name = name
        self.subdivision = 'depot'
        self.__type = Equipment.Type.Printer

    @property
    def get_name(self):
        return self.__name

    @property
    def get_type(self):
        return self.__type

    @abstractmethod
    def __str__(self):
        pass


class Depot:
    def __init__(self, *args):
        """
        Class for deposit equipment
        :param args: list of different type of equipments
        """
        self.equipments = {Equipment.Type.Printer: [],
                           Equipment.Type.Scanner: [],
                           Equipment.Type.Xerox: []}
        for e in args:
            self.add_to_depot(e)

    def __str__(self):
        return f'{[str(j) for i in self.equipments.values() for j in i]}'

    def add_to_depot(self, e: Equipment):
        self.equipments[e.get_type] += [e]

    def send_to_subdiv(self, type_of_eq: Equipment.Type, count: int, subdiv: str):
        """
        Send count of type_of_eq to subdivision
        :param type_of_eq: type of equipment
        :param count: count of equipment
        :param subdiv: subdivision
        :return: sent equipment
        """
        if self.equipments.get(type_of_eq):
            if len(self.equipments[type_of_eq]) >= count:
                temp_eqs = self.equipments[type_of_eq][-count:]
                self.equipments[type_of_eq] = self.equipments[type_of_eq][:-count]
                for equip in temp_eqs:
                    equip.subdivision = subdiv
                return temp_eqs
            else:
                print("На складе недостаточно оборудования данного типа!")
        else:
            print("На складе нет оборудования данного типа!")


class Printer(Equipment):
    def __init__(self, name: str, type_of_cards: int = 0):
        super().__init__(name)
        self.type_of_cards = type_of_cards
        self.__type = Equipment.Type.Printer

    def __str__(self):
        return f'{self.__class__.__name__} name: {self.get_name}; Now in {self.subdivision}; Added by id: {self.id}; ' \
               f'Type of cards: {self.type_of_cards}'


class Scanner(Equipment):
    def __init__(self, name: str, count_of_scans: int = 0):
        super().__init__(name)
        self.__count_of_scans = count_of_scans
        self.__type = Equipment.Type.Scanner

    def __str__(self):
        return f'{self.__class__.__name__} name: {self.get_name}; Now in {self.subdivision}; Added by id: {self.id}; ' \
               f'Count of scans: {self.__count_of_scans}'

    def scan_paper(self):
        self.__count_of_scans += 1


class Xerox(Equipment):
    def __init__(self, name: str, speed: int = 0):
        super().__init__(name)
        self.speed = speed
        self.__type = Equipment.Type.Xerox

    def __str__(self):
        return f'{self.__class__.__name__} name: {self.get_name}; Now in {self.subdivision}; Added by id: {self.id}; ' \
               f'Speed: {self.speed}'


depot = Depot(Xerox('X12'), Scanner('S01'), Printer('P01'))
print(depot)
depot.add_to_depot(Xerox('X02'))
print(depot)
sent_xerox = depot.send_to_subdiv(Equipment.Type.Xerox, 2, 'Finance')
for sx in sent_xerox:
    print(sx)
print(depot)

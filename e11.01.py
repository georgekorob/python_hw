"""
1.	Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый — с декоратором @classmethod. Он должен извлекать число, месяц,
год и преобразовывать их тип к типу «Число». Второй — с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""


class Date:
    def __init__(self, date: str):
        """
        Date class from string
        :param date: d-m-Y
        """
        values = Date.convert(date)
        if values:
            self.day, self.month, self.year = values

    def __str__(self):
        return f'{self.day:02d}-{self.month:02d}-{self.year:04d}'

    @classmethod
    def convert(cls, date):
        if isinstance(date, str):
            values = date.split('-')
            if len(values) == 3:
                values = list(map(int, values))
                if Date.valid(*values):
                    return values

    @staticmethod
    def valid(day, month, year):
        if isinstance(year, int) and isinstance(month, int) and isinstance(day, int) and month > 0 and day > 0:
            if month < 13:
                if (month in [1, 3, 5, 7, 8, 10, 12] and day < 32) or \
                        (month in [4, 6, 9, 11] and day < 31) or \
                        (month == 2 and ((year % 4 == 0 and day < 30) or (day < 29))):
                    return True
        return False


date_test = Date('2-3-2391')
print(date_test)
print(date_test.day)
print(type(date_test.day))

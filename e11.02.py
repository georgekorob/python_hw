"""
2.	Создать собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверить его работу на данных, 
вводимых пользователем. При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию 
и не завершиться с ошибкой.
"""


class ZeroDivisError(ZeroDivisionError):
    def __init__(self, txt):
        self.txt = txt


def try_ex(value):
    try:
        value = int(value)
        print(1 / value)
    except ZeroDivisionError:
        raise ZeroDivisError('Деление на 0!')


div = input('Введите делитель: ')
try:
    try_ex(div)
except Exception as err:
    print(f'Значение {div} выдает ошибку: {err}')

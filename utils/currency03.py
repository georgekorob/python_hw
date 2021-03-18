"""
3. * (вместо 2) Доработать функцию currency_rates(): теперь она должна возвращать кроме курса дату,
которая передаётся в ответе сервера. Дата должна быть в виде объекта date. Подумайте,
как извлечь дату из ответа, какой тип данных лучше использовать в ответе функции?
"""
import requests
import datetime
from decimal import *


def currency_rates(cur_code):
    """
    Функция возвращает курс валюты по её коду
    :param cur_code: Код валюты
    :return: Курс валюты
    """
    # Код из методички (на лекции не было объяснено про requests, хотя этой библиотеке нужно уделить особое внимание)
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = requests.utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    # Можно использовать словарь, но это было бы уместнее в случае, если аргумент был бы списком
    # В нашем случае после нахождения курса данные больше не нужны
    # Дату можно узнать из поля Date
    date, content = content.split('Date="', 2)[1].split('"', 1)
    date = datetime.datetime.strptime(date, "%d.%m.%Y").date()
    while 1:
        # Находим поле с кодом валюты
        spl_str = content.split('CharCode', 2)
        if len(spl_str) < 3:
            return None  # Код не найден
        code = spl_str[1][1:-2]
        # Находим поле со значением валюты
        value = spl_str[2].split('Value')[1][1:-2]
        if code == cur_code.upper():
            # Обычно с денежными велечинами используют Decimal, потому что он точнее хранит дробные числа
            return {'code': code, 'date': date, 'exc': Decimal(value.replace(',', '.'))}
        else:
            content = spl_str[2]


if __name__ == '__main__':
    print(currency_rates('usd'))
    print(currency_rates('EUR'))
    print(currency_rates('rfd'))

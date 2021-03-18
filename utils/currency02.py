"""
2. Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (USD, EUR, ...) и возвращающую курс
этой валюты по отношению к рублю. Использовать библиотеку requests. В качестве API можно использовать
http://www.cbr.ru/scripts/XML_daily.asp. Рекомендация: выполнить предварительно запрос к API в обычном браузере,
посмотреть содержимое ответа. Можно ли, используя только методы класса str, решить поставленную задачу? Функция
должна возвращать результат числового типа, например float. Подумайте: есть ли смысл для работы с денежными величинами
использовать вместо float тип Decimal? Сильно ли усложняется код функции при этом? Если в качестве аргумента передали
код валюты, которого нет в ответе, вернуть None. Можно ли сделать работу функции не зависящей от того, в каком
регистре был передан аргумент? В качестве примера выведите курсы доллара и евро.
"""
import requests
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
            return Decimal(value.replace(',', '.'))
        else:
            content = spl_str[2]


if __name__ == '__main__':
    print(currency_rates('usd'))
    print(currency_rates('EUR'))
    print(currency_rates('rfd'))

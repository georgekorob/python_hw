"""1. Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения извлекает
имя пользователя и почтовый домен из email адреса и возвращает их в виде словаря. Если адрес не валиден,
выбросить исключение ValueError. Пример:
#>>> email_parse('someone@geekbrains.ru')
{'username': 'someone', 'domain': 'geekbrains.ru'}
#>>> email_parse('someone@geekbrainsru')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  ...
    raise ValueError(msg)
ValueError: wrong email: someone@geekbrainsru
Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном выражении;
имеет ли смысл в данном случае использовать функцию re.compile()?
"""
import re


# re.compile() использовать имеет смысл, если вызовов будт очень много
def email_parse(email_address):
    match = re.search(r'^(?P<username>[^@]+?)@(?P<domain>[^\.]+\..+?)$', email_address)
    if match:
        dict_sob = match.groupdict()
        print(dict_sob)
        return dict_sob
    else:
        raise ValueError(f'wrong email: {email_address}')


email_parse('someone@geekbrains.ru.re')
email_parse('someone@geekbrainsru')

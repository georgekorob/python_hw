"""
По значению найти ключ в словаре
"""
test_dict = {'zero': 'ноль',
             'one': 'один',
             'two': 'два',
             'three': 'три',
             'four': 'четыре',
             'five': 'пять',
             'six': 'шесть',
             'seven': 'семь',
             'eight': 'восемь',
             'nine': 'девять',
             'ten': 'десять'}


def search_key(t_dict, value):
    for k, v in t_dict.items():
        if v == value:
            return k
    return None


print(search_key(test_dict, 'семь'))
print(search_key(test_dict, 'осемь'))

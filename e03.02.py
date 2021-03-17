"""
2. * (вместо задачи 1) Доработать предыдущую функцию num_translate_adv(): реализовать корректную работу с числительными,
начинающимися с заглавной буквы. Например:
//>>> >>> num_translate_adv("One")
"Один"
//>>> num_translate_adv("two")
"два"
"""


def num_translate_adv(word):
    """
    Функция перевода числительного c английского на русский язык
    :param word: Введите числительное от 0 до 10 на английском языке в виде строки
    :return: Возвращает перевод слова, строку на русском языке. None, если перевод сделать невозможно
    """
    # Запомним наличие первой прописной буквы
    is_first_char_upper = word[0].isupper()
    # Приведем слово к нижнему регистру
    word = word.lower()
    dic_en_to_ru = {'zero': 'ноль',
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
    # Вернем русское слово с прописной или строчной буквой
    return dic_en_to_ru.get(word).capitalize() if is_first_char_upper else dic_en_to_ru.get(word)


print(num_translate_adv('zer3o'))
print(num_translate_adv('Seven'))
print(num_translate_adv('three'))

# 1. Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield, например:
# >>> odd_to_15 = odd_nums(15)
# >>> next(odd_to_15)
# 1
# >>> next(odd_to_15)
# 3
# ...
# >>> next(odd_to_15)
# 15
# >>> next(odd_to_15)
# ...StopIteration...
from write_gen import print_gen


def odd_nums(num):
    """
    Генератор нечетных чисел
    :param num: До какого числа (включительно)
    :return: Возвращает генератор
    """
    for n in range(num + 1):
        if n % 2:
            yield n


# Инициализация генератора
odd_to_15 = odd_nums(15)

# Вывод значений генератора
print_gen(odd_to_15)

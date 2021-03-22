# 2. * (вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield.
from write_gen import print_gen


def odd_nums(num):
    """
    Генератор нечетных чисел
    :param num: До какого числа (включительно)
    :return: Возвращает генератор
    """
    return (n for n in range(num + 1) if n % 2)


# Инициализация генератора
odd_to_15 = odd_nums(15)

# Вывод значений генератора
print_gen(odd_to_15)

"""3. Написать декоратор для логирования типов позиционных аргументов функции, например:
def type_logger...
    ...


@type_logger
def calc_cube(x):
   return x ** 3

#>>> a = calc_cube(5)
5: <class 'int'>
Примечание: если аргументов несколько - выводить данные о каждом через запятую;
можете ли вы вывести тип значения функции? Сможете ли решить задачу для именованных аргументов?
Сможете ли вы замаскировать работу декоратора? Сможете ли вывести имя функции, например, в виде:
#>>> a = calc_cube(5)
calc_cube(5: <class 'int'>)
"""


def type_logger(func):
    def wrapper(*args, **kwargs):
        # Позиционные и именованные аргументы через запятую
        types = ', '.join(f'{a}: {type(a)}' for a in args + tuple(kwargs.values()))
        result = func(*args, **kwargs)
        # Имя функции выводится, типы аргументов и тип значения функции тоже
        print(f'{func.__name__}({types})={type(result)}')
        # Возвращаем результат
        return result

    return wrapper


@type_logger
def calc_cube(x, y=1):
    return (x * y) ** 3


print(calc_cube(5, y=1))

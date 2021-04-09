"""4. Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные значения функции и
выбрасывать исключение ValueError, если что-то не так, например:
def val_checker...
    ...


@val_checker(lambda x: x > 0)
def calc_cube(x):
   return x ** 3


#>>> a = calc_cube(5)
125
#>>> a = calc_cube(-5)
Traceback (most recent call last):
  ...
    raise ValueError(msg)
ValueError: wrong val -5
Примечание: сможете ли вы замаскировать работу декоратора?
"""


def val_checker(callback):
    def checker(func):
        def wrapper(x):
            # Проверка декоратором используя функцию callback = lambda x: x > 0
            if callback(x):
                return func(x)
            else:
                raise ValueError(f'wrong val {x}')

        return wrapper

    return checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


print(calc_cube(5))
print(calc_cube(-5))

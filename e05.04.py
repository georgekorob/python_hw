# ### 4. Представлен список чисел. Необходимо вывести те его элементы, значения которых больше предыдущего, например:
# src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# result = [12, 44, 4, 10, 78, 123]
# ```
#
# Подсказка: использовать возможности python, изученные на уроке.
from write_gen import print_gen

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]


# Оптимизация по памяти
def val_grater_gen(src_list):
    return (src_list[i] for i in range(1, len(src_list)) if src_list[i] > src_list[i - 1])


# Оптимизация по скорости
def val_grater_list(src_list):
    return [src_list[i] for i in range(1, len(src_list)) if src_list[i] > src_list[i - 1]]


res_gen = val_grater_gen(src)  # Инициализация генератора
print_gen(res_gen)  # Вывод значений генератора

res_list = val_grater_list(src)  # Инициализация списка
print("Список:\t\t", *res_list)  # Вывод значений списка

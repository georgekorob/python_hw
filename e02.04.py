"""
4. Подумать, какое условие записать, чтобы выявить числа среди элементов списка?
Как модифицировать это условие для чисел со знаком?
Дан список, содержащий искажённые данные с должностями и именами сотрудников:
['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
'токарь высшего разряда нИКОЛАй', 'директор аэлита']

Известно, что имя сотрудника всегда в конце строки.
Сформировать и вывести на экран фразы вида:
'Привет, Игорь!' Подумать, как получить имена сотрудников из элементов списка,
как привести их к корректному виду. Можно ли при этом не создавать новый список?
"""
list_of_workers = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй',
                   'директор аэлита']
for i, w in enumerate(list_of_workers):
    # Приводим весь текст к нижнему регистру
    w.lower()
    # Формируем список, чтобы выделить последний элемент
    mass = w.split(' ')
    # Собираем строку с форматированием
    list_of_workers[i] = ' '.join(mass[:-1]).capitalize() + ', ' + mass[-1].capitalize()
    print(list_of_workers[i])

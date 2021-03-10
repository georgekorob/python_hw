"""
2. Дан список:
['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
Необходимо его обработать — обособить каждое целое число кавычками и дополнить нулём до двух разрядов:
['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура',
'воздуха', 'была', '"', '+05', '"', 'градусов']
Новый список не создавать! Сформировать из обработанного списка строку:
в "05" часов "17" минут температура воздуха была "+05" градусов
"""
# Исходный массив
phrase = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

# Создаем новый массив и добавляем элементы
res = []
for el in phrase:
    # Если присутствует знак, а остальное является числом
    if el[0] in ['+', '-'] and el[1:].isdigit():
        if len(el) == 2:
            res += ['"', el[0] + f'{int(el[1:]):02d}', '"']
        else:
            res += ['"', el, '"']
    elif el.isdigit():
        res += ['"', f'{int(el):02d}', '"']
    else:
        res += [el]
print(f'Обработанный список:\t{res}')

# Для формирования строки, которая соответствует заданию,
# кавычки необходимо поместить внутрь элемента для упрощения вывода
for i in range(1, len(res) - 1):
    if i == len(res):
        break
    if res[i] == '"':
        res[i] = ''.join(res[i:i + 3])
        del res[i + 1]
        del res[i + 1]
print('Сформированная строка:\t' + ' '.join(res))

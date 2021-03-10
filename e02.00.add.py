test_list = ['Hello', 42.00000014, True, [1, 2, 3], 1, 2, 'Basil']
"""
Доп задача -> убрать [1,2,3] и заменить на элементы большого списка 1, 2, 3 
в том же месте
Подсказка: index, insert, remove (опционально) 
"""
# Выполнение в одну строку
print(f'Метод "В одну строку":\n{test_list[:3] + test_list[3] + test_list[4:]}\n')

# Выполнение с использованием методов массива
for el in test_list[3][::-1]:
    test_list.insert(4, el)
test_list.remove(test_list[3])
print(f'Метод "С использованием функций":\n{test_list}')

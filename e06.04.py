"""4. * (вместо 3) Решить задачу 3 для ситуации, когда объём данных в файлах превышает объём ОЗУ
(разумеется, не нужно реально создавать такие большие файлы, это просто задел на будущее проекта). 
Также реализовать парсинг данных из файлов - получить отдельно фамилию, имя и отчество для пользователей 
и название каждого хобби: преобразовать в какой-нибудь контейнерный тип (список, кортеж, множество, словарь). 
Обосновать выбор типа. Подумать, какие могут возникнуть проблемы при парсинге. 
В словаре должны храниться данные, полученные в результате парсинга."""

import json

# Читаем файлы по синхронно по одной строке
with open("users.csv", "r", encoding='utf-8') as fu:
    with open("hobby.csv", "r", encoding='utf-8') as fh:
        with open('users_hobby.json_list', 'w', encoding='utf-8') as fd:
            while True:
                user = fu.readline()
                hobby = fh.readline()
                # Завершаем чтение если данных нет
                if not user and not hobby:
                    break
                # Завершаем чтение если данных о пользователях меньше, чем о хобби
                elif not user:
                    print("1")
                    break
                user = user.strip().split(',')
                hobby = hobby.strip().split(',') if hobby else None
                # Для сохранения был выбран тип словаря, чтобы данные были более понятными
                user_hobby = {"ФИО": user, "Хобби": hobby}
                # Запись в файл производится построчно, чтобы не загружать ОЗУ
                fd.write(json.dumps(user_hobby)+'\n')
# При таком парсинге мы должны помнить, что формат файла не универсальный json,
# потому что он хранит строки с объектами json
with open('users_hobby.json_list', 'r', encoding='utf-8') as f:
    line = f.readline().strip()
    while line:
        print(json.loads(line))
        line = f.readline().strip()

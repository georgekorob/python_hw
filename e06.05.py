"""5. ** (вместо 4) Решить задачу 4 и реализовать интерфейс командной строки, чтобы можно было задать путь
к обоим исходным файлам и путь к выходному файлу со словарём. Проверить работу скрипта для случая, 
когда все файлы находятся в разных папках."""

import json
import sys

l_argv = len(sys.argv)
file_users = sys.argv[1] if l_argv > 1 else "users.csv"
file_hobbies = sys.argv[2] if l_argv > 2 else "hobby.csv"
file_dict = sys.argv[3] if l_argv > 3 else "users_hobby.json_list"
# Читаем файлы по синхронно по одной строке
with open(file_users, "r", encoding='utf-8') as fu:
    with open(file_hobbies, "r", encoding='utf-8') as fh:
        with open(file_dict, 'w', encoding='utf-8') as fd:
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
                fd.write(json.dumps(user_hobby) + '\n')
# При таком парсинге мы должны помнить, что формат файла не универсальный json,
# потому что он хранит строки с объектами json
with open(file_dict, 'r', encoding='utf-8') as f:
    line = f.readline().strip()
    while line:
        print(json.loads(line))
        line = f.readline().strip()

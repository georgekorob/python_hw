"""4. Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи —
верхняя граница размера файла (пусть будет кратна 10), а значения — общее количество файлов
(в том числе и в подпапках), размер которых не превышает этой границы, но больше предыдущей (начинаем с 0), например:
    {
      100: 15,
      1000: 3,
      10000: 7,
      100000: 2
    }
Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.
5. * (вместо 4) Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи те же,
а значения — кортежи вида (<files_quantity>, [<files_extensions_list>]), например:
  {
      100: (15, ['txt']),
      1000: (3, ['py', 'txt']),
      10000: (7, ['html', 'css']),
      100000: (2, ['png', 'jpg'])
    }
Сохраните результаты в файл <folder_name>_summary.json в той же папке, где запустили скрипт."""

import os
import json


# Вложения папок представляют деревья, удобно воспользоваться рекурсией
def get_stat_files(main_path):
    listdir = os.listdir(main_path)
    list_files = []
    if listdir:
        for file in listdir:
            # Полный путь к файлу
            file_path = os.path.join(main_path, file)
            if os.path.isdir(file_path):
                # Если папка, то ищем фалы дальше
                list_files += get_stat_files(file_path)
            else:
                list_files += [(os.stat(file_path).st_size, os.path.splitext(file_path)[1])]
    return list_files


path = os.getcwd()
list_sizes = get_stat_files(path)
dict_stat = {}
for l in list_sizes:
    for n in range(1, 20):
        key = 10 ** n
        if l[0] < key:
            if dict_stat.get(key):
                dict_stat[key] = (dict_stat[key][0] + 1, list(set(dict_stat[key][1] + [l[1]])))
            else:
                dict_stat[key] = (1, [l[1]])
            break

# JSON не умеет сериализовать множество, поэтому используем массив
res_dict = {k: dict_stat[k] for k in sorted(dict_stat)}
name_file = f'{os.path.split(path)[-1]}_summary.json'
with open(name_file, 'w') as f:
    json.dump(res_dict, f)
with open(name_file, 'r') as f:
    data = json.load(f)
print(data)

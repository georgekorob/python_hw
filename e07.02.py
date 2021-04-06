"""2. * (вместо 1) Написать скрипт, создающий из config.yaml стартер для проекта со следующей структурой:
|--my_project
   |--settings
   |  |--__init__.py
   |  |--dev.py
   |  |--prod.py
   |--mainapp
   |  |--__init__.py
   |  |--models.py
   |  |--views.py
   |  |--templates
   |     |--mainapp
   |        |--base.html
   |        |--index.html
   |--authapp
   |  |--__init__.py
   |  |--models.py
   |  |--views.py
   |  |--templates
   |     |--authapp
   |        |--base.html
   |        |--index.html
Примечание: структуру файла config.yaml придумайте сами, его можно создать в любом текстовом редакторе «руками»
(не программно); предусмотреть возможные исключительные ситуации, библиотеки использовать нельзя.
"""
import os


class NestedError(Exception):
    pass


with open('config.yaml', 'r') as f:
    frl = f.readline().strip()
    paths = []
    while frl:
        inp = len(paths)
        # Ищем глубину вложенности
        count = frl.count('-')
        for c in range(count + 1)[::-1]:
            if frl.startswith('-' * c):
                # Файл или папка находится по соседству
                if c == inp:
                    paths = paths[:-1] + [frl.strip('-')]
                # Файл или папка находится в данной папке
                elif c == inp + 1:
                    paths += [frl.strip('-')]
                # Файл или папка находится выше данной папки
                elif c < inp:
                    paths = paths[:c - inp - 1] + [frl.strip('-')]
                # Ошибка структуры вложенности файла
                else:
                    raise NestedError
                # Адрес папки или файла
                file_or_dir = os.path.join(*paths)
                if '.' in file_or_dir:
                    with open(file_or_dir, 'w') as tf:
                        pass
                else:
                    os.makedirs(file_or_dir, exist_ok=True)
                frl = f.readline().strip()
                break

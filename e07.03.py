"""3. Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике).
Написать скрипт, который собирает все шаблоны в одну папку templates, например:
|--my_project
   ...
  |--templates
   |   |--mainapp
   |   |  |--base.html
   |   |  |--index.html
   |   |--authapp
   |      |--base.html
   |      |--index.html
Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы расположены в родительских папках
(они играют роль пространств имён); предусмотреть возможные исключительные ситуации; это реальная задача,
которая решена, например, во фреймворке django.
"""
import os
import shutil


# Вложения папок представляют деревья, удобно воспользоваться рекурсией
def templates_move(main, cur_folder):
    listdir = os.listdir(cur_folder)
    if listdir:
        for file in listdir:
            # Полный путь к файлу
            file_path = os.path.join(cur_folder, file)
            if os.path.isdir(file_path):
                # Если папка, то ищем фалы дальше
                templates_move(main, file_path)
            elif file.endswith('.html'):
                # Создаем папку пространства имен, если её нет
                new_path = os.path.join(main, *cur_folder.split('\\')[-1:])
                os.makedirs(new_path, exist_ok=True)
                new_path = os.path.join(new_path, file)
                try:
                    # Попытка копирования
                    shutil.copy(file_path, new_path)
                except shutil.SameFileError:
                    pass


folder = os.path.join(os.getcwd(), 'my_project')
templates_move(os.path.join(folder, 'templates'), folder)

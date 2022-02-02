# __autor__ = Kupp Evgenii


# Задача 3
# Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике). Написать
# скрипт, который собирает все шаблоны в одну папку templates, например:
# |--my_project
#    ...
#    |--templates
#    |   |--authapp
#    |   |  |--base.html
#    |   |  |--index.html
#    |   |--authapp
#    |      |--base.html
#    |      |--index.html
#
#
# Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы расположены в родительских папках
# (они играют роль пространств имён); предусмотреть возможные исключительные ситуации; это реальная задача, которая
# решена, например, во фреймворке django.

# Решение
import os
import shutil


root = os.path.join(os.getcwd(), 'my_project')
folder_1 = os.path.join(os.getcwd(), 'my_project', 'templates')
os.makedirs(folder_1, exist_ok=True)
for root, dirs, files in os.walk(root):
    print(root)
    if root.count('templates'):
        for d in dirs:
            os.makedirs(os.path.join(folder_1, d), exist_ok=True)
        for f in files:
            path_f = os.path.join(root, f)
            dir_f = os.path.join(folder_1, os.path.basename(root))
            if os.path.dirname(path_f) != dir_f:
                shutil.copy(path_f, dir_f)

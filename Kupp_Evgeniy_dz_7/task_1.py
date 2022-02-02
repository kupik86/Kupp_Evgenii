# __autor__ = Kupp Evgenii


# Задача 1
# Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
# |--my_project
#    |--settings
#    |--authapp
#    |--adminapp
#    |--authapp
#
#
# Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?); как лучше хранить конфигурацию
# этого стартера, чтобы в будущем можно было менять имена папок под конкретный проект; можно ли будет при этом расширять
# конфигурацию и хранить данные о вложенных папках и файлах (добавлять детали)?

# Решение
import os


root = os.getcwd()
folder = 'my_project'
if not os.path.exists(folder):
    list_folders = ['settings', 'authapp', 'adminapp', 'authapp']
    gen = (os.path.join(folder, x) for x in list_folders)
    for i in gen:
        os.makedirs(os.path.join(root, i), exist_ok=True)
else:
    print('Папка с таким именем уже есть')

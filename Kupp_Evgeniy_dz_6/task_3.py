# __autor__ = Kupp Evgenii

# Задача №3
# Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом  — данные об их хобби. Известно, что при
# хранении данных используется принцип: одна строка — один пользователь, разделитель между значениями — запятая.
# Написать код, загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО, значения — данные о
# хобби. Сохранить словарь в файл. Проверить сохранённые данные. Если в файле, хранящем данные о хобби, меньше
# записей, чем в файле с ФИО, задаём в словаре значение None. Если наоборот — выходим из скрипта с кодом «1». При
# решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.
# Фрагмент файла с данными о пользователях (users.csv):
# Иванов,Иван,Иванович
# Петров,Петр,Петрович
# Фрагмент файла с данными о хобби  (hobby.csv):
# скалолазание,охота
# горные лыжи

# Решение
from itertools import zip_longest
import json
import sys


with open('users.csv', 'r', encoding='utf-8') as f1:
    with open('hobby.csv', 'r', encoding='utf-8') as f2:
        with open('logs_f1_f2.json', 'w', encoding='utf-8') as f3:
            users = (f1.read()).split()
            hobby = (f2.read()).split()
            gen = (el for el in zip_longest(users, hobby))
            d = {}
            if len(users) >= len(hobby):
                for key, value in gen:
                    d[key] = value
                json.dump(d, f3, ensure_ascii=False, indent=4)
            else:
                sys.exit(1)
with open('logs_f1_f2.json', 'r', encoding='utf-8') as r:
    result = json.load(r)
print(result)

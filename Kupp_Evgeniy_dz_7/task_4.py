# __autor__ = Kupp Evgenii


# Задача 4
# Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи — верхняя граница
# размера файла (пусть будет кратна 10), а значения — общее количество файлов (в том числе и в подпапках), размер
# которых не превышает этой границы, но больше предыдущей (начинаем с 0), например:
#     {
#       100: 15,
#       1000: 3,
#       10000: 7,
#       100000: 2
#     }
# Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
# Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.

# Решение
import os


def get_stat(folder_path):
    rezult = {}
    for root, _, files in os.walk(folder_path):
        for _fail in files:
            stat = os.stat(os.path.join(root, _fail)).st_size
            key = get_range(stat)
            if key not in rezult:
                rezult[key] = 0
            rezult[key] += 1
    print(rezult)


def get_range(size):
    counter = 1
    size = int(size)
    while True:
        if size // 10 != 0:
            counter += 1
        else:
            break
        size //= 10
    return 10 ** counter


get_stat(r'C:\Users\kupik-PC\PycharmProjects\pythonProject\1 четверть\Kupp_Evgenii\Kupp_Evgeniy_dz_4')

# __autor__ = Kupp Evgenii

# Задача №6
# Реализовать простую систему хранения данных о суммах продаж булочной. Должно быть два скрипта с интерфейсом командной
# строки: для записи данных и для вывода на экран записанных данных. При записи передавать из командной строки значение
# суммы продаж. Для чтения данных реализовать в командной строке следующую логику:
# просто запуск скрипта — выводить все записи;
# запуск скрипта с одним параметром-числом — выводить все записи с номера, равного этому числу, до конца;
# запуск скрипта с двумя числами — выводить записи, начиная с номера, равного первому числу, по номер, равный второму
# числу, включительно.
# Подумать, как избежать чтения всего файла при реализации второго и третьего случаев.
# Данные хранить в файле bakery.csv в кодировке utf-8. Нумерация записей начинается с 1. Примеры запуска скриптов:
# python add_sale.py 5978,5
# python add_sale.py 8914,3
# python add_sale.py 7879,1
# python add_sale.py 1573,7
# python show_sales.py
# 5978,5
# 8914,3
# 7879,1
# 1573,7
# python show_sales.py 3
# 7879,1
# 1573,7
# python show_sales.py 1 3
# 5978,5
# 8914,3
# 7879,1

# Решение
# sales.py
# import sys
#
#
# sales = sys.argv[1]
# with open('bakery.csv', 'a', encoding='utf-8') as f1:
#     print(sales, file=f1)

from sys import argv


with open('bakery.csv', 'r', encoding='utf-8') as f2:
    conditions = len(argv)
    if conditions == 1:
        print(f2.read())
    elif conditions == 2:
        for el in f2.readlines()[int(argv[1]) - 1:]:
            print(el, end='')
    elif conditions == 3:
        for el in f2.readlines()[int(argv[1]) - 1:int(argv[2])]:
            print(el, end='')

# __autor__ = Kupp Evgenii

# Задача №1
# Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) — получить список
# кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:
# [
#     ...
#     ('141.138.90.60', 'GET', '/downloads/product_2'),
#     ('141.138.90.60', 'GET', '/downloads/product_2'),
#     ('173.255.199.22', 'GET', '/downloads/product_2'),
#     ...
# ]

# Решение
# import pathlib
#
# p = pathlib.Path('nginx_logs.txt')
# print(p)
with open('nginx_logs.txt', 'r', encoding='UTF-8') as f:
    txt = f.read()
    # for el in f:
    #     slova = el.split()

    print(txt)

# __autor__ = Kupp Evgenii

# Задача №2
# *(вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из предыдущего задания.
# Примечание: спамер — это клиент, отправивший больше всех запросов; код должен работать даже с файлами, размер которых
# превышает объем ОЗУ компьютера.


# Решение
d = {}
value_max = 0
key_result = None
with open('nginx_logs.txt', 'r', encoding='UTF-8') as f:
    for lines in f:
        el = lines.split()
        if el[0] in d:
            d[el[0]] += 1
        else:
            d[el[0]] = 1
for key, value in d.items():
    if value > value_max:
        value_max = value
        key_result = key
print(f'Спамер найден \nIP: {key_result} \nчисло запросов: {value_max}')

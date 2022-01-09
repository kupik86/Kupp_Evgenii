# __autor__ = Kupp Evgenii

# Задача №3
# * (вместо 2) Доработать функцию currency_rates(): теперь она должна возвращать кроме курса дату, которая передаётся
# в ответе сервера. Дата должна быть в виде объекта date. Подумайте, как извлечь дату из ответа, какой тип данных
# лучше использовать в ответе функции?

# Решение
import requests
import datetime


def currency_rates(item):
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    respone = requests.get(url)
    # определяем кодировку страницы и декодируем ее, приводя содержимое к строковому типу
    content = respone.content.decode(encoding=respone.encoding)
    item = item.upper()
    # Дорабатываем функцию: теперь она возвращает кроме курса дату, которая передаётся в ответе сервера.
    time_data = respone.headers
    data = time_data['Date']
    data_format = datetime.datetime.strptime(data, '%a, %d %b %Y %H:%M:%S %Z').date()
    rezult = None
    if item not in content:
        return rezult
    else:
        el_1 = content.split(f'{item}')[1]  # отрезаем от строки все лишнее до искомой валюты
        el_2 = el_1.split('</Value>')[0]  # отрезаем от строки все лишнее после стоимости искомой валюты
        # вычленяем из строки стоимость приводим ее к числовому типу данных и округляем до 2 разрядов
        rezult = round(float(el_2.split('<Value>')[1].replace(',', '.')), 2)
        return f'Курс валюты {rezult} руб. {data_format}'


if __name__ == '__main__':
    money = input('Введите валюту: ')
    print(currency_rates(money))

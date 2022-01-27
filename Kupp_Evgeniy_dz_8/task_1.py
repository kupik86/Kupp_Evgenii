# __autor__ = Kupp Evgeniy


# Задача 1
# Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения извлекает имя пользователя
# и почтовый домен из email адреса и возвращает их в виде словаря. Если адрес не валиден, выбросить исключение
# ValueError. Пример:
# >>> email_parse('someone@geekbrains.ru')
# {'username': 'someone', 'domain': 'geekbrains.ru'}
# >>> email_parse('someone@geekbrainsru')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   ...
#     raise ValueError(msg)
# ValueError: wrong email: someone@geekbrainsru
#
#
# Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном выражении; имеет ли
# смысл в данном случае использовать функцию re.compile()?

# Решение
import re


def email_parse(e_mail):
    assert pattern.match(e_mail), f'ValueError: wrong email:{e_mail}'
    rez = pattern.finditer(e_mail)
    for group in rez:
        print(group.groupdict())


pattern = re.compile(r'(?P<username>.+)[@](?P<domain>[a-z]+\.[a-z]+)')
email_parse('Kupp56@gmail.com')

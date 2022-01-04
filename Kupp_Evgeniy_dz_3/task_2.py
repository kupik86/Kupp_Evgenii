# __autor__ = Kupp Evgenii

# Задача 2
# * (вместо задачи 1) Доработать предыдущую функцию в num_translate_adv(): реализовать корректную работу с
# числительными, начинающимися с заглавной буквы — результат тоже должен быть с заглавной. Например:
# >>> num_translate_adv("One")
# "Один"
# >>> num_translate_adv("two")
# "два"

# Решение
def num_translate(x):
    numbers_en = {
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'zero': 'ноль',
        'ten': 'десять'
    }
    return numbers_en.get(x)


en = input('Введите число на английском языке: ')
if en.istitle():  # Определяем с заглавной буквы ввод или нет. Если да, то...
    en = en.lower()
    # если ввести с заглавной значение, которого нет в словаре, идет None. Создаем условие чтобы ее обработать
    if num_translate(en):
        print(num_translate(en).capitalize())
    else:
        print(num_translate(en))
else:  # Если не с заглавной буквы ввод, тогда ...
    print(num_translate(en))

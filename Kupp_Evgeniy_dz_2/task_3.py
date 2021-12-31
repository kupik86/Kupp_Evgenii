# __autor__ = Kupp Evgenii

# Задача
# 3. Дан список:
# ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
#
# Необходимо его обработать — обособить каждое целое число (вещественные не трогаем) кавычками (добавить кавычку до
# и кавычку после элемента списка, являющегося числом) и дополнить нулём до двух целочисленных разрядов:
# ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
#
# Сформировать из обработанного списка строку:
# в "05" часов "17" минут температура воздуха была "+05" градусов
#
# Подумать, какое условие записать, чтобы выявить числа среди элементов списка? Как модифицировать это условие для
# чисел со знаком?
# Примечание: если обособление чисел кавычками не будет получаться - можете вернуться к его реализации позже. Главное:
# дополнить числа до двух разрядов нулём!
# * Решить задачу не создавая новый список (как говорят, in place). Эта задача намного серьёзнее, чем может сначала
# показаться.

# Решение
""" list_data - изначальный список элементов; number - проверяемый элемент списка;
 r- разряд ( сколько нолей дабавляем )
"""


def update(list_data, number, r):
    pos = list_data.index(number)  # определяем индекс найденного элемента
    quotation_marks = f'"{number.zfill(r)}"'  # формируем строку из элемента вложенного в двойные кавычки и
    # обновленного в соответствии с разрядом
    list_data.remove(number)  # удаляем исходный элемент из редактируемого списка
    list_data.insert(pos, quotation_marks)  # заменяем удаленный элемент на обновленный


elements = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
for find_numbers in elements:  # создаем цикл для проверки условий
    if find_numbers.startswith('+') or find_numbers.startswith('-'):  # проверяем элементы где указан знак + или -
        update(elements, find_numbers, 3)  # обновляем элементы по заданию
    if find_numbers.isdigit():  # находим в списке числа
        update(elements, find_numbers, 2)  # обновляем элементы по заданию
print(' '.join(elements))  # выводим результат в строку

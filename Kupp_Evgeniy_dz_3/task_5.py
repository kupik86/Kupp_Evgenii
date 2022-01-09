# __autor__ = Kupp Evgenii

# Задача 5
# Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов, взятых из трёх списков
# (по одному из каждого):
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
#         Например:
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]

# Решение
import random


def get_jokes(y):
    jokes = []
    for i in range(y):
        el_n = random.choice(nouns)
        el_av = random.choice(adverbs)
        el_aj = random.choice(adjectives)
        sequence = f'{el_n} {el_av} {el_aj}'
        jokes.append(sequence)
    print(jokes)


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

get_jokes(int(input('введите количество шуток: ')))

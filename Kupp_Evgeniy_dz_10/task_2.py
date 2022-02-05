# __autor__ = Kupp Evgeniy


# Задача 2
# Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта
# — одежда, которая может иметь определённое название. К типам одежды в этом проекте относятся пальто и костюм. У этих
# типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H,
# соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма
# (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Выполнить общий подсчёт расхода ткани. Проверить на практике полученные на этом уроке знания. Реализовать абстрактные
# классы для основных классов проекта и проверить работу декоратора @property.

# Решение
class Coat:
    def __init__(self, title, size):
        self.title = title
        self.size = size
        Clothes.sum_cloth_lst.append(round((self.size / 6.5 + 0.5), 1))

    def __str__(self):
        return f'{round((self.size / 6.5 + 0.5), 1)} м ткани уйдет чтобы сшить {self.title}'


class Suit:
    def __init__(self, title, size):
        self.title = title
        self.size = size
        Clothes.sum_cloth_lst.append(round((self.size * 2 + 0.3), 1))

    def __str__(self):
        return f'{round((self.size * 2 + 0.3), 1)} м ткани уйдет чтобы сшить {self.title}'


class Clothes(Coat, Suit):
    sum_cloth_lst = []

    @staticmethod
    def sum_cloth():
        return f'Всего потребуется ткани {sum(Clothes.sum_cloth_lst)} м'


suit_1 = Suit('пиджак', 1.7)
suit_2 = Suit('фрак', 1.9)
coat_1 = Coat('зимнее пальто', 52)
print(suit_1)
print(suit_2)
print(coat_1)
print(Clothes.sum_cloth())

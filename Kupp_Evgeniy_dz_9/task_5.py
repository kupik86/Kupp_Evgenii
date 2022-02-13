# __autor__ = Kupp Evgeniy


# Задача 5
# Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное
# сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

# Решение
class Stationery:
    title = 'Канцелярская принадлежность'

    def draw(self):
        return f'Запуск отрисовки'


class Pen(Stationery):
    def __init__(self, title):
        self.title = title

    def draw(self):
        return 'не пишет, срержень закончился'


class Pencil(Stationery):
    def __init__(self, title):
        self.title = title

    def draw(self):
        return '(перед использованием) нужно заточить'


class Handle(Stationery):
    def __init__(self, title):
        self.title = title

    def draw(self):
        return 'на вкус и цвет у каждого разные'


pen = Pen('Ручка гелевая')
print(pen.title, pen.draw())
pencil = Pencil('Карандаш')
print(pencil.title, pencil.draw())
handle = Handle('Фломастеры')
print(handle.title, handle.draw())

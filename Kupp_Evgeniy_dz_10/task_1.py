# __autor__ = Kupp Evgeniy


# Задача 1
# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
# принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
# | 31 22 |
# | 37 43 |
# | 51 86 |
#
# | 3 5 32 |
# | 2 4 6 |
# | -1 64 -8 |
#
# | 3 5 8 3 |
# | 8 3 7 1 |
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для сложения двух объектов класса Matrix (двух матриц). Результатом
# сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно. Первый элемент первой строки первой матрицы складываем
# с первым элементом первой строки второй матрицы и пр.

# Решение
class Matrix:
    def __init__(self, *args):
        self.lists = []
        self.lists_int = [*args]
        for i in args:
            self.lists.append(str(i))

    def __str__(self):
        return '\n'.join(self.lists)

    def __add__(self, other):
        r = []
        for i in zip(self.lists_int, other.lists_int):
            c = []
            for h in range(len(self.lists_int[0])):
                g = (i[0][h] + i[1][h])
                c.append(g)
            r.append(str(c))
        return Matrix('\n'.join(r))


obj_1 = Matrix([1, 2, 3, 2], [4, 5, 6, 5], [8, 1, 3, 1], [8, 1, 3, 4])
obj_2 = Matrix([3, 2, 1, 1], [6, 5, 4, 4], [6, 8, 4, 4], [8, 1, 3, 1])
print(f'{obj_1}\n\n{obj_2}')
print(f'\n{obj_1 + obj_2}')

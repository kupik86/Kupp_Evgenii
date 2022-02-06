# __autor__ = Kupp Evgeniy


# Задача
# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверьте его работу на данных,
# вводимых пользователем. При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не
# завершиться с ошибкой.

# Решение
class MyErr(Exception):
    pass


class MyClass:
    def __init__(self, number_1, number_2):
        self.number_1 = int(number_1)
        self.number_2 = int(number_2)
        self.res = self.calculation(number_1, number_2)

    @staticmethod
    def calculation(number_1, number_2):
        try:
            if number_2 == 0:
                raise MyErr(f'на {number_2} делить нельзя')
        except MyErr as err:
            return err
        else:
            res = int(number_1 / number_2)
            return res

    def __str__(self):
        return f'{self.res}'


my_1 = MyClass(12, 2)
print(my_1)
my_2 = MyClass(12, 0)
print(my_2)
my_3 = MyClass(0, 45)
print(my_3)

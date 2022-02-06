# __autor__ = Kupp Evgeniy


# Задача
# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверьте его работу на данных,
# вводимых пользователем. При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не
# завершиться с ошибкой.

# Решение
class MyErr(Exception):
    pass


def calculation():
    number_1 = int(input('введите первое число: '))
    number_2 = int(input('введите второе число: '))
    try:
        if number_2 == 0:
            raise MyErr(f'на {number_2} делить нельзя')
    except MyErr as err:
        print(err)
    else:
        res = number_1 / number_2
        print(res)


calculation()

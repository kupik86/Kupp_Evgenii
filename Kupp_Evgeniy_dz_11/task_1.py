# __autor__ = Kupp Evgeniy


# Задача 1
# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год
# и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

# Решение
class MyError1(Exception):
    pass


class MyError2(Exception):
    pass


class Date:
    def __init__(self, date):
        self.date = Date.from_date_to_numbers(date)

    @staticmethod
    def validate(date):
        try:
            if not (1 <= date['day'] <= 31):
                raise MyError1(f'{date["day"]} - измените день')
        except MyError1 as err1:
            print(err1)
        else:
            try:
                if not (1 <= date["month"] <= 12):
                    raise MyError2(f'{date["month"]} - измените месяц')
            except MyError2:
                return False
            else:
                return True
        finally:
            try:
                if not (1 <= date["month"] <= 12):
                    raise MyError2(f'{date["month"]} - измените месяц')
            except MyError2 as err2:
                print(err2)

    @classmethod
    def from_date_to_numbers(cls, date):
        day, month, year = map(int, date.split('-'))
        return {'day': day, 'month': month, 'year': year}

    def __str__(self):
        if self.validate(self.date):
            return f'{self.date["day"]}.{self.date["month"]}.{self.date["year"]}'
        else:
            return f'неверный формат даты'


date_1 = Date('14-13-2022')
print(date_1)
date_2 = Date('33-16-2013')
print(date_2)
date_3 = Date('05-02-1923')
print(date_3)
date_4 = Date('45-12-1980')
print(date_4)
date_5 = Date('12-13-2223')
print(date_5)

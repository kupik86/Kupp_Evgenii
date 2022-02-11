# __autor__ = Kupp Evgeniy


# Задача 4
# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определите параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры,
# уникальные для каждого типа оргтехники.
#
# Решение
class WareHouse:
    position = 'Москва'


class OfficeEquipment:
    paper = 'A4'
    color = 'white'
    voltage = 220


class Scanner(OfficeEquipment):
    scan_file = True


class Printer(OfficeEquipment):
    print_file = True


class Xerox(OfficeEquipment):
    copy_file = True

# __autor__ = Kupp Evgeniy


# Задача 5
# Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники на склад и
# передачу в определённое подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру (например, словарь).

# Решение
class WareHouse:
    position = 'Москва'
    in_warehouse = {'scanner': 0, 'printer': 0, 'xerox': 0}
    in_office_1 = {'scanner': 0, 'printer': 0, 'xerox': 0}
    in_office_2 = {'scanner': 0, 'printer': 0, 'xerox': 0}
    in_office_3 = {'scanner': 0, 'printer': 0, 'xerox': 0}

    @staticmethod
    def position_office_equipment():
        f = {'склад': WareHouse.in_warehouse, 'офис_1': WareHouse.in_office_1, 'офис_2': WareHouse.in_office_2,
             'офис_3': WareHouse.in_office_3}
        for x, y in f.items():
            print(x, y)


class MyErr1(Exception):
    pass


class MyErr2(Exception):
    pass


class OfficeEquipment:
    paper = 'A4'
    color = 'white'
    voltage = 220

    def __init__(self, name_obj):
        self.name_obj = name_obj

    def send_to_the_warehouse(self, quantity):
        WareHouse.in_warehouse[self.name_obj] += int(quantity)

    @classmethod
    def send_to_the_office(cls, name_obj, quantity, office):
        try:
            if WareHouse.in_warehouse[name_obj] < int(quantity):
                raise MyErr2(f'оборудования в количестве {quantity} ед. нет на складе')
        except MyErr2 as err:
            print(err)
        else:
            WareHouse.in_warehouse[name_obj] = int(WareHouse.in_warehouse[name_obj]) - int(quantity)
            if office == 'офис_1':
                WareHouse.in_office_1[name_obj] = int(WareHouse.in_office_1[name_obj]) + int(quantity)
            elif office == 'офис_2':
                WareHouse.in_office_2[name_obj] = int(WareHouse.in_office_2[name_obj]) + int(quantity)
            elif office == 'офис_3':
                WareHouse.in_office_3[name_obj] = int(WareHouse.in_office_3[name_obj]) + int(quantity)


class Scanner(OfficeEquipment):
    scan_file = True


class Printer(OfficeEquipment):
    print_file = True


class Xerox(OfficeEquipment):
    copy_file = True


obj_1 = Scanner('scanner')
obj_1.send_to_the_warehouse(4)
print(WareHouse.in_warehouse)
obj_1.send_to_the_warehouse(5)
print(WareHouse.in_warehouse)
obj_1.send_to_the_office('scanner', 3, 'офис_1')
print(WareHouse.in_warehouse)
print(WareHouse.in_office_1)
obj_1.send_to_the_office('scanner', 6, 'офис_2')
print(WareHouse.position_office_equipment())
obj_1.send_to_the_office('scanner', 6, 'офис_2')
obj_2 = Printer('printer')
obj_2.send_to_the_warehouse(22)
obj_3 = Xerox('xerox')
obj_3.send_to_the_warehouse(15)
print(WareHouse.position_office_equipment())
obj_3.send_to_the_office('xerox', 5, 'офис_3')
print(WareHouse.position_office_equipment())

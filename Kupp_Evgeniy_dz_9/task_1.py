# __autor__ = Kupp Evgeniy


# Задача 1.
# Создать класс TrafficLight (светофор).
# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный)
# — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении выводить соответствующее сообщение и
# завершать скрипт.

# Решение
import time
import turtle


class TrafficLight:
    # __color = ['red', 'yellow', 'green']
    __color = 'red'

    def running(self):
        turtle.dot(100, self.__color)
        # z = 7
        # for i in TrafficLight.__color:
        #     turtle.dot(100, i)
        #     time.sleep(z)
        #     z = 2


color_red = TrafficLight()
color_red.running()
time.sleep(7)
color_yellow = TrafficLight()
color_yellow._TrafficLight__color = 'yellow'
color_yellow.running()
time.sleep(2)
color_green = TrafficLight()
color_green._TrafficLight__color = 'green'
color_green.running()
time.sleep(1)

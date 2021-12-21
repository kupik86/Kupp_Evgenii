# __autor__ = Kupp Evgenii

# Задача №1
# 1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в
# секундах: до минуты: <s> сек; до часа: <m> мин <s> сек; до суток: <h> час <m> мин <s> сек; * в остальных
# случаях: <d> дн <h> час <m> мин <s> сек.

# Решение
time = []
duration = int(input("Введите промежуток времени: "))
day = duration // 86400
hour = duration % 86400 // 3600
mines = duration % 3600 // 60
sek = duration % 60
data = {"дн ": day, "час ": hour, "мин ": mines, "сек": sek}
for meaning, key in data.items():
    if key != 0:
        time.append(key)
        time.append(meaning)
print(" ".join(map(str, time)))
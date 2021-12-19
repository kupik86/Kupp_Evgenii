# __autor__ = Kupp Evgenii

# 1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в
# секундах: до минуты: <s> сек; до часа: <m> мин <s> сек; до суток: <h> час <m> мин <s> сек; * в остальных
# случаях: <d> дн <h> час <m> мин <s> сек.

# Решение
time = []
duration = 154688
day = duration // 86400
hour = duration % 86400 // 3600
min = duration % 3600 // 60
sek = duration % 60
data = {"дн ": day, "час ": hour, "мин ": min, "сек": sek}
for meaning, key in data.items():
    if key != 0:
        time.append(key)
        time.append(meaning)
print(" ".join(map(str, time)))


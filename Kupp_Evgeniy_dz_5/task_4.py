# __autor__ = Kupp Evgenii

# Задача 4
# Представлен список чисел. Необходимо вывести те его элементы, значения которых больше предыдущего, например:
# src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# result = [12, 44, 4, 10, 78, 123]
# ```

# Решение
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
rezult = []
gen = (y for y in src)
for x in src[1:]:
    if x > next(gen):
        rezult.append(x)
print(rezult)

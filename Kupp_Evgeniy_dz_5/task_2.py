# __autor__ = Kupp Evgenii

# Задача 2
# Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield, например:
# >>> odd_to_15 = odd_nums(15)
# >>> next(odd_to_15)
# 1
# >>> next(odd_to_15)
# 3
# ...
# >>> next(odd_to_15)
# 15
# >>> next(odd_to_15)
# ...StopIteration...
# * (вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield.

# Решение
odd_nums = 15
odd_to_15 = (i for i in range(1, odd_nums + 1) if i % 2 != 0)
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))

# __autor__ = Kupp Evgenii

# Задача №5
# * (вместо 4) Доработать скрипт из предыдущего задания: теперь он должен работать и из консоли. Например:
# > python task_4_5.py USD
# 75.18, 2020-09-05

# Решение
import sys
import task_3


# cansole = sys.argv
print(task_3.currency_rates(sys.argv[1]))

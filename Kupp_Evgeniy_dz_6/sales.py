import sys


sales = sys.argv[1]
with open('bakery.csv', 'a', encoding='utf-8') as f1:
    print(sales, file=f1)

# __autor__ = Kupp Evgenii

# Задача 4
# * (вместо задачи 3) Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки в формате
# «Имя Фамилия» и возвращающую словарь, в котором ключи — первые буквы фамилий, а значения — словари, реализованные
# по схеме предыдущего задания и содержащие записи, в которых фамилия начинается с соответствующей буквы. Например:
# >>>thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
# {"А": {"П": ["Петр Алексеев"]}, "С": {"И": ["Иван Сергеев", "Инна Серова"], "А": ["Анна Савельева"]}}
# Как поступить, если потребуется сортировка по ключам?

# Решение
def reversed_name(rev_name):
    sort_list = []
    rev_name = list(rev_name)
    for sort_name in rev_name:
        step_1 = str(sort_name).split(' ')
        step_1.reverse()
        h = ' '.join(step_1)
        sort_list.append(h)
    return sort_list


def thesaurus(args):
    slovar = {}
    slv = list(args)
    sorted(slv)
    for name in slv:
        fst_letter = name[0]
        if slovar.get(fst_letter):
            slovar[fst_letter].append(name)
        else:
            slovar.setdefault(fst_letter, [name])
    return slovar


def thesaurus_adv(*args):
    revesred_args = reversed_name(args)
    revesred_args.sort()
    z = []
    for key, value in thesaurus(revesred_args).items():
        value_sl = thesaurus(reversed_name(value))
        u = {key: value_sl}
        z.append(u)
    b = {}
    for el in z:
        b.update(el)
    print(b)


thesaurus_adv('Маша Петрова', 'Антон Петров', 'Петя Антонов', 'Вася Прохоров', 'Коля Анисимов', 'Митя Парфенов',
              'Витя Рожков', 'Костя Демидов')

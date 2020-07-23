"""
Задание 2.

Реализуйте два алгоритма.

Первый, в виде функции, должен обеспечивать поиск минимального значения для списка.
В основе алгоритма должно быть сравнение каждого числа со всеми другими элементами списка.
Сложность такого алгоритма: O(n^2) - квадратичная.

Второй, в виде функции, должен обеспечивать поиск минимального значения для списка.
Сложность такого алгоритма: O(n) - линейная.

Примечание:
Построить список можно через генератор списка.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.
"""

# ----------------------------var 1---------------------------------------
import random


def min_el(list_el):
    min_val = 100
    for iter1 in enumerate(list_el):
        for iter2 in enumerate(list_el):
            if iter1[1] < iter2[1] and iter1[1] < min_val:
                min_val = iter1[1]
    return min_val


elements = [random.randint(1, 99) for i in range(1, 15)]
print(elements)
print(min_el(elements))

# -----------------------------var 2--------------------------------------


def min_el_two(list_el):
    return min(list_el)


lst = [random.randint(1, 99) for i in range(1, 15)]
print(elements)
print(min_el_two(elements))

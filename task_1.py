"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. Обязательно доработайте алгоритм (сделайте его умнее).

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение
Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию

Разница в замерах не существенная и не постоянная, зависит от загруженности процессора.
Выйгрыш по времени только на один проход цикла. Его не возможно заметить ))
"""


import random
import timeit


def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def bubble_sort_2(arr):
    for i in range(len(arr)):
        flag = True
        for j in range(len(arr) - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                flag = False
        if flag:
            break


# замер 20
list_el = [random.randint(-100, 100) for i in range(1, 20)]
print(
    timeit.timeit(
        "bubble_sort(list_el)",
        setup="from __main__ import bubble_sort, list_el",
        number=1))
# замер 200
list_el = [random.randint(-100, 100) for i in range(1, 200)]
print(
    timeit.timeit(
        "bubble_sort(list_el)",
        setup="from __main__ import bubble_sort, list_el",
        number=1))
# замер 2000
list_el = [random.randint(-100, 100) for i in range(1, 2000)]
print(
    timeit.timeit(
        "bubble_sort(list_el)",
        setup="from __main__ import bubble_sort, list_el",
        number=1))
# замер 5000
list_el = [random.randint(-100, 100) for i in range(1, 5000)]
print(
    timeit.timeit(
        "bubble_sort(list_el)",
        setup="from __main__ import bubble_sort, list_el",
        number=1))

# замер 20
list_el = [random.randint(-100, 100) for i in range(1, 20)]
print(
    timeit.timeit(
        "bubble_sort_2(list_el)",
        setup="from __main__ import bubble_sort_2, list_el",
        number=1))
# замер 200
list_el = [random.randint(-100, 100) for i in range(1, 200)]
print(
    timeit.timeit(
        "bubble_sort_2(list_el)",
        setup="from __main__ import bubble_sort_2, list_el",
        number=1))
# замер 2000
list_el = [random.randint(-100, 100) for i in range(1, 2000)]
print(
    timeit.timeit(
        "bubble_sort_2(list_el)",
        setup="from __main__ import bubble_sort_2, list_el",
        number=1))
# замер 5000
list_el = [random.randint(-100, 100) for i in range(1, 5000)]
print(
    timeit.timeit(
        "bubble_sort_2(list_el)",
        setup="from __main__ import bubble_sort_2, list_el",
        number=1))

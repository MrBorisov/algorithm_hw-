"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.

Задачу можно решить без сортировки исходного
массива.

Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, ...

arr[m]
from statistics import median
"""
import random
import copy
from statistics import median

def find_mediana(unsrt_lst):
    i = 0
    for i in range(len(unsrt_lst)):
        unsrt_lst_copy = copy.copy(unsrt_lst)
        left_lst = []
        right_lst = []
        my_mediana = unsrt_lst_copy.pop(i)
        for el in unsrt_lst_copy:
            if el > my_mediana:
                right_lst.append(el)
            elif el < my_mediana:
                left_lst.append(el)
            elif el == my_mediana:



        if len(left_lst) == len(right_lst) and max(left_lst) <= my_mediana and min(right_lst) >= my_mediana:
            break
        else:
            i +=1
    return my_mediana

m = 3
unsrt_lst = [random.randint(0, 100) for i in range(m * 2 + 1)]
print(unsrt_lst)
print(sorted(unsrt_lst))
print(find_mediana(unsrt_lst))
print(median(unsrt_lst))


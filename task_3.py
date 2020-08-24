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
    left_lst = []
    right_lst = []
    temp = unsrt_lst
    for i in range(len(temp)):
        for j in range(len(temp)):
            if temp[i] > temp[j]:
                left_lst.append(temp[j])
            if temp[i] < temp[j]:
                right_lst.append(temp[j])
            if temp[i] == temp[j] and i > j:
                left_lst.append(temp[j])
            if temp[i] == temp[j] and i < j:
                right_lst.append(temp[j])
        if len(left_lst) == len(right_lst):
            return temp[i]
        left_lst.clear()
        right_lst.clear()

m = 3

for i in range(100):
    unsrt_lst = [random.randint(0, 100) for i in range(m * 2 + 1)]
    if find_mediana(unsrt_lst) != median(unsrt_lst):
        print(unsrt_lst)
        print(sorted(unsrt_lst))
        print(find_mediana(unsrt_lst))
        print(median(unsrt_lst))
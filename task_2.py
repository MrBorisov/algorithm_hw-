"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.


"""
import random


def merge(lst_lft, lst_rgh):
    res = []
    i = 0
    j = 0
    while i < len(lst_lft) and j < len(lst_rgh):
        if lst_lft[i] <= lst_rgh[j]:
            res.append(lst_lft[i])
            i += 1
        else:
            res.append(lst_rgh[j])
            j += 1
    res += lst_lft[i:] + lst_rgh[j:]
    return res


def mergesort(lst_unsrt):
    if len(lst_unsrt) <= 1:
        return lst_unsrt
    else:
        lst_lft = lst_unsrt[:len(lst_unsrt) // 2]
        lst_rgh = lst_unsrt[len(lst_unsrt) // 2:]
    return merge(mergesort(lst_lft), mergesort(lst_rgh))


list_el = [random.uniform(0, 50) for i in range(1, 10)]

print(f'исходный {list_el}')
print(f'отсортированный {mergesort(list_el)}')

"""
Задание 1.
Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Можно взять задачи с курса Основ или с текущего курса Алгоритмов

Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""
from memory_profiler import profile
import random
import copy
import hashlib

@profile
def hhh():
    user_string = input('Введите строку: ')

    subs_lst = set()

    for i in range(len(user_string)):
        for j in range(i, len(user_string)):
            subs_lst.add(hashlib.sha1(
                user_string[i:j + 1].encode('utf-8')).hexdigest())

    print('Количество неповторяющихся подстрок - ', len(list(subs_lst)))
hhh()

'''
Line #    Mem usage    Increment   Line Contents
================================================
    21     15.4 MiB     15.4 MiB   @profile
    22                             def hhh():
    23     15.5 MiB      0.0 MiB       user_string = input('Введите строку: ')
    24                             
    25     15.5 MiB      0.0 MiB       subs_lst = set()
    26                             
    27     15.5 MiB      0.0 MiB       for i in range(len(user_string)):
    28     15.5 MiB      0.0 MiB           for j in range(i, len(user_string)):
    29     15.5 MiB      0.0 MiB               subs_lst.add(hashlib.sha1(
    30     15.5 MiB      0.0 MiB                   user_string[i:j + 1].encode('utf-8')).hexdigest())
    31                             
    32     15.5 MiB      0.0 MiB       print('Количество неповторяющихся подстрок - ', len(list(subs_lst)))



Process finished with exit code 0
тут не чему увеличивать память, мы не генерируем новые данные, ма работаем с массивом, введенным пользователем.
'''

@profile
def min_el():
    list_el = [random.randint(1, 999) for i in range(1, 900)]
    min_val = 1000
    for iter1 in enumerate(list_el):
        for iter2 in enumerate(list_el):
            if iter1[1] < iter2[1] and iter1[1] < min_val:
                min_val = copy.deepcopy(iter1[1])
    del list_el
    return min_val
print(min_el())

'''
Line #    Mem usage    Increment   Line Contents
================================================
    10     15.4 MiB     15.4 MiB   @profile
    11                             def min_el():
    12     15.4 MiB      0.0 MiB       list_el = [random.randint(1, 999) for i in range(1, 900)]
    13     15.4 MiB      0.0 MiB       min_val = 1000
    14     15.5 MiB      0.0 MiB       for iter1 in enumerate(list_el):
    15     15.5 MiB      0.0 MiB           for iter2 in enumerate(list_el):
    16     15.5 MiB      0.0 MiB               if iter1[1] < iter2[1] and iter1[1] < min_val:
    17     15.4 MiB      0.0 MiB                   min_val = copy.deepcopy(iter1[1])
    18     15.5 MiB      0.0 MiB       del list_el
    19     15.5 MiB      0.0 MiB       return min_val
    
    тут тоже ни чего не растет и не уменьшается даже при удалении массива. странно...
'''

@profile
def min_el():
    list_el = [random.randint(1, 999) for i in range(1, 150)]
    for element_1 in list_el:
        is_min = True
        for element_2 in list_el:
            if element_1 > element_2:
                is_min = False
        if is_min:
            del list_el
            return element_1

print(min_el())

'''
Line #    Mem usage    Increment   Line Contents
================================================
    10     15.4 MiB     15.4 MiB   @profile
    11                             def min_el():
    12     15.4 MiB      0.0 MiB       list_el = [random.randint(1, 999) for i in range(1, 150)]
    13     15.4 MiB      0.0 MiB       for element_1 in list_el:
    14     15.4 MiB      0.0 MiB           is_min = True
    15     15.4 MiB      0.0 MiB           for element_2 in list_el:
    16     15.4 MiB      0.0 MiB               if element_1 > element_2:
    17     15.4 MiB      0.0 MiB                   is_min = False
    18     15.4 MiB      0.0 MiB           if is_min:
    19     15.4 MiB      0.0 MiB               del list_el
    20     15.4 MiB      0.0 MiB               return element_1


9

Process finished with exit code 0
я пока не могу найти задачу в которой бы память увеличивалась. в этой, аналогично предыдущим не генерируются данные.
'''
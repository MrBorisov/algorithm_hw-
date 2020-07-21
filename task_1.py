"""
Задание 1.

Для каждой из трех задач выполнить следующее:

1) для каждой инструкции рядом в комментарии определите сложность этой инструкции
2) определите сложность алгоритма в целом

укажите сложность непосредственно в этом файле
точки, где нужно поработать вам, отмечены знаком '!!!'

Примечание:
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.
"""

import random


#############################################################################################
def check_1(lst_obj):
    """Функция должна создать множество из списка.

    Алгоритм 3:
    Создать множество из списка

    Сложность: !!!.
    """
    lst_to_set = set(lst_obj)  # !!! константа операция присваивания всегда константа
    return lst_to_set


#############################################################################################
def check_2(lst_obj):
    """Функция должная вернуть True, если все элементы списка различаются.

    Алгоритм 1:
    Проходимся по списку и для каждого элемента проверяем,
    что такой элемент отстутствует
    в оставшихся справа элементах

    Сложность: !!! Линейная. количество сравнений растет линейно с ростом n
    """
    for j in range(len(lst_obj)):          # !!! Линейная O(n)
        if lst_obj[j] in lst_obj[j+1:]:    # !!! константа
            return False                   # !!! константа
    return True                            # !!! константа


#############################################################################################
def check_3(lst_obj):
    """Функция должная вернуть True, если все элементы списка различаются.

    Алгоритм 2:
    Вначале выполним для списка сортировку, далее, сравниваем элементы попарно
    Если присутствуют дубли, они будут находиться рядом.

    Сложность: !!! Линейная O(n) так как сравнений будет n-1 и при росте n будет линейный рост количества сравнений
    """
    lst_copy = list(lst_obj)                 # !!! константа
    lst_copy.sort()                          # !!! O(nlog n) согласно документации
    for i in range(len(lst_obj) - 1):        # !!! O(n-1), можно O(n), len(lst) константа, согласно документации
        if lst_copy[i] == lst_copy[i+1]:     # !!! константа
            return False                     # !!! константа
    return True                              # !!! константа

#############################################################################################


for j in (50, 500, 1000, 5000, 1000):
    # Из 100000 чисел возьмем 'j' случайно выбранных
    # Всего 10 тыс. чисел
    lst = random.sample(range(-100000, 100000), j) # O(n) линейная, всегда будет выполняться n раз

print(check_1(lst))
print(check_2(lst))
print(check_3(lst))

"""Сравним цикл и рекурсию"""


def get_sum_1(lst_obj):
    """Простой цикл"""

    res = 0
    for el in lst_obj:
        res = res + el
    return res


def get_sum_2(lst_obj):
    """Простая рекурсия"""
    if len(lst_obj) == 1:
        return lst_obj[0]
    else:
        return lst_obj[0] + get_sum_2(lst_obj[1:])


print(get_sum_1([1, 3, 5, 7, 9]))
print(get_sum_2([1, 3, 5, 7, 9]))

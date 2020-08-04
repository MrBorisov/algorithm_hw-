"""
Задание 1.

Докажите, что словари обрабатываются быстрее, чем списки.

Реализуйте две функции, в первой нужно заполнить элементами список, во второй-словарь
Сделайте замеры времени выполнения каждой из функций

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к двум своим функциям.
"""
import time


def lst_append(num, lst=None):
    '''

    :param num: int количество элементов
    :param lst: список
    :return: сиписок
    '''
    lst(num)
    return lst


def dict_append(num):
    '''

    :param num: int количество элементов
    :param test_dict: словарь
    :return: словарь
    '''
    test_dict = {a: a ** 2 for a in range(num)}
    return test_dict


def check_1(num):
    """
    Фиксируем отсечки времени до и после выполнения основной логики
    :param num:
    :return: кортеж из результата ф-ции и затраченного времени
    """

    start_val = time.time()
    lst_append(num)
    end_val = time.time()
    lst_val = end_val - start_val

    start_val = time.time()
    dict_append(num)
    end_val = time.time()
    dict_val = end_val - start_val

    return f'список наполнялся {lst_val}, а словарь {dict_val}'


print(check_1(1000000))

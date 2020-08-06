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


def benchmark(func):
    '''
    замеряем время исполнения функции
    :param func:
    :return: время исполнения
    '''

    def wrapper(*args, **kwargs):
        '''

        :param args:
        :param kwargs:
        :return:
        '''
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        all_time = end - start
        print('[*] Время выполнения:')
        return all_time

    return wrapper


@benchmark
def lst_append(num, lst=None):
    '''

    :param num: int количество элементов
    :param lst: список
    :return: сиписок
    '''
    lst = [i for i in range(num)]


@benchmark
def dict_append(num):
    '''

    :param num: int количество элементов
    :param test_dict: словарь
    :return: словарь
    '''
    test_dict = {a: a ** 2 for a in range(num)}


print(f'list {lst_append(1000000)}')
print(f'dict  {dict_append(1000000)}')

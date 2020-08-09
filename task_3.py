"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
revers_3 самый быстрый способ, так как он является встроенным и оптимизирован.
самый медленный - рекурсия ибо она всегда медленная ей еще приходится
память занимать своими вызовами, цикл сопоставим со срезом, но слегка медленней.
"""

from timeit import timeit
import cProfile


def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def main():
    revers(1231234567)
    revers_2(1231234567)
    revers_3(1231234567)


cProfile.run('main()')

print(
    timeit(
        "revers(1231234567)",
        setup="from __main__ import revers",
        number=1))
print(
    timeit(
        "revers_2(1231234567)",
        setup="from __main__ import revers_2",
        number=1))
print(
    timeit(
        "revers_3(1231234567)",
        setup="from __main__ import revers_3",
        number=1))

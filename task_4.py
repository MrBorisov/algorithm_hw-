"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


def summ_of_elem(counter, num=1, sum_els=0):
    if counter > 0:
        counter -= 1
        sum_els = sum_els + num
        num = num / 2
        return summ_of_elem(counter, num, sum_els)
    else:
        print(sum_els)
        return sum_els


try:
    numb = int(input('введите число: '))
except ValueError:
    print('вы ввели не число')
print(f'сумма = {summ_of_elem(numb)}')

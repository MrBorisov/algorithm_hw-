"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.

 Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""
def check():
    """
    функция проверки ввода пользователя
    :return: возвращает число
    """
    try:
        number = int(input('введите число: '))
    except ValueError:
        print('вы ввели не число')
    return number

def proof(number, sum_of_numbers=0):
    if number == 0:
        return sum_of_numbers
    else:
        sum_of_numbers + number
        number -= 1
        return proof(number, sum_of_numbers=0)
number = check()
print(number*(number + 1)/2)
print(proof(number))
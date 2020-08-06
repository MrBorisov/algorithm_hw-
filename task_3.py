"""
Задание 3.
Определить количество различных подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.

Подсказка: примените хеши и множества
"""
import hashlib
user_string = input('Введите строку: ')

subs_lst = set()

for i in range(len(user_string)):
    for j in range(i, len(user_string)):
        subs_lst.add(hashlib.sha1(
            user_string[i:j + 1].encode('utf-8')).hexdigest())

print('Количество неповторяющихся подстрок - ', len(list(subs_lst)))

"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя функцию sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш

Далее программа должна запросить пароль повторно
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль
"""
import hashlib

def hash_the_password(password):
    '''

    :param password: string
    :return: хэш солёного пароля
    '''
    salt = 'l23kj42op3ij09fudjfl3k2jrp94'  # Запомните
    key = hashlib.sha256(password.encode('utf-8') + salt.encode('utf-8'))
    res = key.hexdigest()
    return res
user_password = input('введите пароль: ')
hash_user_password = hash_the_password(user_password)

chek_the_password = input('введите пароль для проверки: ')
hash_chek_password = hash_the_password(chek_the_password)
if hash_user_password == hash_chek_password:
    print(f'пароли совпадают{hash_user_password}')
else:
    print(f'пароли совпадают{hash_user_password}')
    print(f'пароли не совпадают{hash_chek_password}')



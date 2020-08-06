"""
Задание 4.
Реализуйте скрипт "Кеширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""
from uuid import uuid4
import hashlib

url_base = {}


def hash_the_site(url):
    '''

    :param url: string
    :return: хэш солёного utl
    '''
    salt = uuid4().hex  # Запомните  # Запомните
    key = hashlib.sha256(url.encode('utf-8') + salt.encode('utf-8'))
    res = [key.hexdigest(), salt]
    return res


def check_url_base(url):
    '''

    :param url: string адрес сайта
    :return: текст и список
    '''
    if url_base.get(url):
        print('url уже в базе')
    else:
        url_base[url] = hash_the_site(url)
        print(f'Добавили новый url в базу{url_base}')


check_url_base('www.ya.ru')
check_url_base('www.ya.ru')
check_url_base('www.ta.ru')

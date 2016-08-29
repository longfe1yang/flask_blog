import requests
from my_log import log
import random

host = 'http://127.0.0.1:5000'
# r = requests.get(host)
# log(r.text)
# if r.status_code == '200':
#     log('成功')
# print(r.status_code)


def random_user():
    username = random.randint(100, 999)
    sex = random.choice('male', 'female')
    password = random.randint(100, 999)
    note = random.choice('啦啦啦', '哈哈哈', 'enenna')
    u = {
        'username': username,
        'password': password,
        'sex': sex,
        'note': note
    }
    return u


def post(path, form):
    url = host + path
    r = requests.post(url, json=form)
    return r


def user_add(form):
    path = '/register'
    return post(path, form)


def user_login(form):
    path = '/login'
    return post(path, form)

if __name__ == '__main__':
    # form = {
    #     'username': '123',
    #     'password': '123'
    # }
    # response = user_login(form)
    # log(response.status_code, response.text)
    # path = host + '/api/tweet/deliver'
    # response = requests.get(path)
    # response.encoding = 'utf-8'
    # print(response.status_code, response.text)
    dct = {}


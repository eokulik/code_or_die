import requests


def get_all_posts():
    response = requests.request('GET', 'https://jsonplaceholder.typicode.com/posts').json()
    # print(len(response))
    # print(response[0]['title'])
    # assert 1 == 1, '1 does not equal 1'
    assert len(response) == 100


def get_one_post():
    response = requests.request('GET', 'https://jsonplaceholder.typicode.com/posts/11').json()
    print(response['id'])


get_all_posts()
get_one_post()
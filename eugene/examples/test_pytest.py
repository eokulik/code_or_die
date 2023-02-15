import pytest
import requests


@pytest.fixture()
def base_url():
    return 'https://jsonplaceholder.typicode.com'


@pytest.fixture(scope='session')  # ``"class"``, ``"module"``, ``"package"`` or ``"session"``
def print_smth():
    print('BEFORE')
    yield None
    print('AFTER')


def test_get_all_posts(base_url):
    print('TEST1')
    response = requests.request('GET', f'{base_url}/posts').json()
    assert len(response) == 100, 'Not all posts returned'


def test_get_one_post(base_url, print_smth):
    print('TEST2')
    post_id = 11
    response = requests.request('GET', f'{base_url}/posts/{post_id}').json()
    assert response['id'] == post_id, 'wrong post id'

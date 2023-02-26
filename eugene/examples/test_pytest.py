from datetime import datetime

import pytest
import requests


@pytest.fixture(scope='session')
def base_url():
    # large query
    return 'https://jsonplaceholder.typicode.com'


@pytest.fixture(scope='session')  # ``"class"``, ``"module"``, ``"package"`` or ``"session"`` or ``"function"``
def print_smth():
    print('BEFORE')
    yield None
    print('AFTER')


@pytest.mark.smoke
def test_get_all_posts(base_url):
    print('TEST1')
    response = requests.request('GET', f'{base_url}/posts').json()
    assert len(response) == 100, 'Not all posts returned'


@pytest.mark.parametrize('ids', [11, 20, 33, 42])
@pytest.mark.smoke
def test_get_one_post(base_url, print_smth, ids):
    print('TEST2')
    # post_id = 11
    response = requests.request('GET', f'{base_url}/posts/{ids}').json()
    assert response['id'] == ids, 'wrong post id'


@pytest.mark.skip('feature not implemented')
@pytest.mark.regression
def test_one_one():
    assert 1 == 1


@pytest.mark.skipif(datetime.now().weekday() == 1, reason='not working at tuesdays')
@pytest.mark.regression
def test_two_two():
    assert 2 == 2


def test_three_three():
    assert 3 == 3

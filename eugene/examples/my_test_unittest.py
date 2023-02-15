import unittest
import requests
from datetime import datetime


class TestSimpleCases(unittest.TestCase):

    def setUp(self):
        print('this method will work before every test', end='')

    def tearDown(self):
        print('after each test')

    @unittest.skipIf(datetime.now().weekday() == 2, 'not working at wednesdays')
    def test_get_all_posts(self):
        print('AAAAAA')
        response = requests.request('GET', 'https://jsonplaceholder.typicode.com/posts').json()
        self.assertEqual(len(response), 100, 'Not all posts returned')

    # @unittest.skip('Bug #1323984')
    def test_get_one_post(self):
        print('AAAAAA')
        post_id = 11
        response = requests.request('GET', f'https://jsonplaceholder.typicode.com/posts/{post_id}').json()
        self.assertEqual(response['id'], post_id)


'''
assertEqual(a, b) — a == b
assertNotEqual(a, b) — a != b
assertTrue(x) — bool(x) is True
assertFalse(x) — bool(x) is False
assertIs(a, b) — a is b
assertIsNot(a, b) — a is not b
assertIsNone(x) — x is None
assertIsNotNone(x) — x is not None
assertIn(a, b) — a in b
assertNotIn(a, b) — a not in b
assertIsInstance(a, b) — isinstance(a, b)
assertNotIsInstance(a, b) — not isinstance(a, b)
assertGreater(a, b) — a > b
assertGreaterEqual(a, b) — a >= b
assertLess(a, b) — a < b
assertLessEqual(a, b) — a <= b
'''
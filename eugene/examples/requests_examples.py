import requests
import json


def get_all_posts():
    response = requests.request('GET', 'https://jsonplaceholder.typicode.com/posts').json()
    print(response[0]['title'])


def get_one_post():
    response = requests.request('GET', 'https://jsonplaceholder.typicode.com/posts/11').json()
    print(response['id'])


def add_post():
    my_headers = {
        'Content-Type': 'application/json',
        # 'Authorization': 'skjdhfksjdfhwieuyiwejhsf',
    }
    my_body = json.dumps(
        {
            "userId": 3,
            "id": 15,
            "title": "Code or Die",
            "body": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque vitae placerat dolor, porta semper nulla"
        }
    )
    response = requests.request(
        'POST',
        'https://jsonplaceholder.typicode.com/posts',
        headers=my_headers,
        data=my_body
    ).json()
    print(response)


def delete_post():
    requests.request('DELETE', 'https://jsonplaceholder.typicode.com/posts/40')
    response = requests.request('GET', 'https://jsonplaceholder.typicode.com/posts/40')
    if response.status_code == 404:
        print("Ok")
    else:
        print(f'Failed + {response.status_code}')

delete_post()

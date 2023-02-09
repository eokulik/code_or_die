import json
from urllib import request, error


def get_all_posts():
    req = request.Request('https://jsonplaceholder.typicode.com/posts')
    response = request.urlopen(req)
    response = response.read().decode('utf-8')
    response = json.loads(response)
    print(response[0]['userId'])


def get_one_post():
    req = request.Request('https://jsonplaceholder.typicode.com/posts/42')
    response = request.urlopen(req)
    response = json.load(response)
    print(response['title'])


def add_post():
    req = request.Request('https://jsonplaceholder.typicode.com/posts', method='POST')
    req.add_header('Content-Type', 'application/json')
    # req.add_header('Authorization', 'Bearer lakjsdhflkajsdhfadsafdlkjhf')
    req.data = json.dumps({
        "userId": 3,
        "id": 15,
        "title": "Code or Die",
        "body": (
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
            "Pellentesque vitae placerat dolor, porta semper nulla"
        )
    }).encode('ascii')
    response = json.load(request.urlopen(req))
    print(response)


def update_post():
    req = request.Request('https://jsonplaceholder.typicode.com/posts/42', method='PUT')
    req.add_header('Content-Type', 'application/json')
    req.data = json.dumps({
        "userId": 3,
        "id": 15,
        "title": "Code or Die",
        "body": (
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
            "Pellentesque vitae placerat dolor, porta semper nulla"
        )
    }).encode('ascii')
    response = json.load(request.urlopen(req))
    print(response)


def del_post():
    req = request.Request('https://jsonplaceholder.typicode.com/posts/200', method='DELETE')
    request.urlopen(req)
    req = request.Request('https://jsonplaceholder.typicode.com/posts/200')
    try:
        json.load(request.urlopen(req))
    except error.HTTPError as err:
        if err.code == 404:
            print("Ok")
        else:
            print('Non 404 Error')
    else:
        print('Test Failed')


del_post()

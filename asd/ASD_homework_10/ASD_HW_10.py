import requests


def get_data():
    response = requests.request('GET', 'https://test-apps-ninja01.konturlabs.com/active/api/apps/58851b50-9574-4aec-'
                                       'a3a6-425fa18dcb54/layers').json()
    print(response)


get_data()

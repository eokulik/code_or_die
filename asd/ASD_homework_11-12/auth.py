import json
import requests


def authorize(base_url):
    url = f"{base_url}/authorize"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "name": "asd"
    }
    authorize = requests.post(url, headers=headers, data=json.dumps(data)).text
    json_data = json.loads(authorize)
    asd_token_value = json_data["token"]
    print(asd_token_value)
    return asd_token_value

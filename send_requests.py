import json

import requests

if __name__ == "__main__":
    api_url = 'http://localhost:5000/example/login'
    data = {'user_or_token': 'Ion',
            'password': 'parola1234'}

    r = requests.get(url=api_url, json=data)
    print(r.status_code, r.reason, r.text)
    token = ''
    if r.status_code == 200:
        token = json.loads(r.text)

        token = token["token"]

    api_url = 'http://localhost:5000/example'
    data = {'user_or_token': token,
            'password': ''}

    r = requests.get(url=api_url, json=data)
    print(r.status_code, r.reason, r.text)

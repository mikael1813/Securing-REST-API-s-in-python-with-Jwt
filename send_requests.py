import json
import time

import requests

if __name__ == "__main__":
    api_url = 'http://localhost:5000/example/login'
    create_row_data = {'user_or_token': 'Ion',
                       'password': 'parola1234'}

    r = requests.get(url=api_url, json=create_row_data)
    print(r.status_code, r.reason, r.text)
    token = ''
    if r.status_code == 200:
        token = json.loads(r.text)

        token = token["token"]

    api_url = 'http://localhost:5000/example'
    create_row_data = {'user_or_token': token,
                       'password': ''}

    r = requests.get(url=api_url, json=create_row_data)
    print(r.status_code, r.reason, r.text)

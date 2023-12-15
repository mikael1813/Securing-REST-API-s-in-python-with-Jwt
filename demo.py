import time

import jwt
from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

key = "Gustavo74032TheThird"

user_list = {
    'Ion': 'parola1234',
    'Marcel': 'ursu1990'
}


def generate_auth_token(user, expires_in=600):
    return jwt.encode({'mail': user, 'exp': time.time() + expires_in},
                      key=key, algorithm='HS256')


@app.route('/example/login', methods=["GET"])
@auth.login_required
def login():
    user_or_token = request.json['user_or_token']

    token = generate_auth_token(user_or_token, 4)
    return jsonify({'token': token})


@app.route('/example', methods=["GET"])
@auth.login_required
def sample_method():
    return jsonify({'pickle': 'Pickle Rick', 'duration': 'immortal', 'sourness': 'beyond maximum'})


@auth.verify_password
def verify_password(user_or_token, password):
    user_or_token = request.json['user_or_token']
    password = request.json['password']
    is_token_ok = verify_auth_token(user_or_token)

    if is_token_ok:
        return True
    if user_or_token in user_list:
        if user_list[user_or_token] == password:
            return True

    return False


def verify_auth_token(token):
    try:
        data = jwt.decode(token, key=key,
                          algorithms=['HS256'])
        print(data)
    except Exception as e:
        print(e)
        return False
    return True


if __name__ == '__main__':
    app.run()

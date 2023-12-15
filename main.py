from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/example', methods=["GET"])
def sample_method():
    return jsonify({'pickle': 'Pickle Rick', 'duration': 'immortal', 'sourness': 'beyond maximum'})


if __name__ == '__main__':
    app.run()

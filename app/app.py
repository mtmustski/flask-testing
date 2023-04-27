import os
from flask import Flask, jsonify

app = Flask(__name__)

env_name = os.environ.get('ENV_NAME', '.env did not load')


@app.route('/')
def index():
    data = {'env_name': f'{env_name}'}
    return jsonify(data)


@app.route('/hello')
def hello():
    return jsonify({'hello': 'world'})


if __name__ == "__main__":
    app.run()

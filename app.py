import os
from flask import Flask, request, jsonify, make_response
from flask_cors import CORS

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
STATIC_PATH = os.path.join(ROOT_PATH, 'dist')

app = Flask(__name__, static_folder=STATIC_PATH, static_url_path='')
CORS(app)

@app.route('/')
def response_test():
    return app.send_static_file('index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
# coding: utf-8
from flask import Flask, Response, request
import bjoern

from database import find_all, insert


app = Flask(__name__)


@app.route('/hello')
def hello_world():
    return 'Hello World!'


@app.route('/', methods=['GET'])
def find():
    rows = find_all()
    resp = Response(None, status=200, mimetype='application/json')
    resp.data = rows
    return resp


@app.route('/', methods=['POST'])
def add():
    data = request.data
    insert(data)
    return Response(None, status=201, mimetype='application/json')


if __name__ == '__main__':
    bjoern.listen(app, '0.0.0.0', 8080)
    bjoern.run()

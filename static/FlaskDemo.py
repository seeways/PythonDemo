# coding=utf-8
from flask import Flask

app = Flask(__name__)


@app.route('/get/taoyuan')
def hello_world():
    return "Hello World!"


if __name__ == '__main__':
    app.run()

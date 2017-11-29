# coding=utf-8
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello World! \n Test Two"


if __name__ == '__main__':
    app.run()

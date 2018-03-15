from flask import Flask, render_template,request

import shell
from data import REDIS

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/command', methods=['GET', 'POST'])
def command():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()

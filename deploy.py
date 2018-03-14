from flask import Flask, render_template,request
import shell

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/command', methods=['GET', 'POST'])
def command():
    a=request.form["command"]
    shell.shell(a)
    return render_template('index.html')


if __name__ == '__main__':
    app.run()

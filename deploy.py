#!/usr/bin/env python
# encoding: utf-8

# @Time         : 2018/3/15 上午11:28
# @Author       : zk
# @Mail         : zk1006@live.cn
# @File         : settings.py
# @description  : 配置信息

from flask import Flask, render_template,request
from flask_socketio import SocketIO, emit
import json
from model import pro,pro_path
from data import REDIS
import shell

app = Flask(__name__, static_url_path='')
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/index')
def index():
    return render_template('index.html')


# 跳转配置页面
@app.route('/toSetting')
def to_setting():
    return render_template('setting.html')


# 添加配置信息
@app.route('/setting', methods=['GET', 'POST'])
def setting():
    path_list = request.form.getlist("path")
    tomcat_list = request.form.getlist("tomcatPath")

    base_svn_path = request.form["baseSvnPath"]
    pro_name = request.form["pro"]
    project_bak = request.form["projectBak"]
    list = []
    for i in range(len(path_list)):
        list.append(pro_path(path_list[i], tomcat_list[i]))

    project = pro(base_svn_path, pro_name, project_bak, json.dumps(list))

    print(json.dumps(project))
    # REDIS.add(pro_name, project.__dict__)
    return render_template('index.html')


@app.route('/command', methods=['GET', 'POST'])
def command():
    comm = request.form["command"]
    shell.exec_cmd(comm)
    return render_template('index.html')


# 根据配置升级项目
@app.route('/upProject', methods=['GET', 'POST'])
def up_project():
    return render_template('index.html')


# @socketio.on('my event', namespace='/operaLog')
# def test_message(message):
#     emit('my response', {'data': message['data']})
#
#
# @socketio.on('my broadcast event', namespace='/operaLog')
# def test_message(message):
#     emit('my response', {'data': message['data']}, broadcast=True)
#
#
# @socketio.on('connect', namespace='/operaLog')
# def test_connect():
#     res = subprocess.Popen(['tail','-f','/tmp/deploy.tmp.log'], shell=True, stdout=subprocess.PIPE)
#     while True:
#         data = res.stdout.readline()
#         if data == b'':
#             if res.poll() is not None:
#                 break
#         else:
#             print(res.stdout.readline().decode())
#             emit('my response', {'data': res.stdout.readline().decode()}, broadcast=True)
#
#
# #断开连接
# @socketio.on('disconnect', namespace='/operaLog')
# def test_disconnect():
#     print('Client disconnected')


if __name__ == '__main__':
    app.run(port=8888)

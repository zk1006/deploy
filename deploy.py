#!/usr/bin/env python3
# encoding: utf-8

# @Time         : 2018/3/15 上午11:28
# @Author       : zk
# @Mail         : zk1006@live.cn
# @File         : settings.py
# @description  : 配置信息

from flask import Flask, render_template, request
from model import pro
from data import REDIS
import upProject
import shell
import sys

app = Flask(__name__, static_url_path='')


@app.route('/')
def index():
    keys = REDIS().get_keys()
    return render_template('index.html', keys=keys)


# 跳转配置页面
@app.route('/toSetting')
def to_setting():
    return render_template('setting.html')


# 添加配置信息
@app.route('/setting', methods=['GET', 'POST'])
def setting():
    path_list = request.form.getlist("path")
    tomcat_list = request.form.getlist("tomcatPath")
    name_list = request.form.getlist("name")
    base_svn_path = request.form["baseSvnPath"]
    pro_name = request.form["pro"]
    project_bak = request.form["projectBak"]
    list = []
    for i in range(len(path_list)):
        list.append({'svn_path': path_list[i], 'tomcat_path': tomcat_list[i], "name": name_list[i]})
    project = pro(base_svn_path, pro_name, project_bak, list)
    REDIS().add(pro_name, project.__dict__)
    return render_template('index.html')


@app.route('/command', methods=['GET', 'POST'])
def command():
    comm = request.form["command"]
    shell.exec_cmd(comm)
    return render_template('index.html')


# 根据配置升级项目
@app.route('/upProject', methods=['GET', 'POST'])
def up_project():
    key = request.form['key']
    up_pros = request.form.getlist("pro")
    projects = eval(REDIS().get(key))
    pro_list = []
    api_list = []
    for project in projects["pro"]:
        for up_pro in up_pros:
            if project["svn_path"] == up_pro and project["tomcat_path"] == '':
                api_list.append(up_pro)
            elif project["svn_path"] == up_pro and project["tomcat_path"] != '':
                pro_list.append({'tomcat': project["tomcat_path"], 'path': up_pro, 'name': project["name"]})
    upProject.up_pro(api_list, projects["base_svn_path"], projects["bak_path"])
    upProject.up_pro(pro_list, projects["base_svn_path"], projects["bak_path"])
    return render_template('index.html')


@app.route('/toUpProject', methods=['GET'])
def to_up_project():
    key = request.values['key']
    project = eval(REDIS().get(key))
    return render_template('upProject.html', project=project, key=key)


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
    shell.exec_cmd("chmod 777 "+sys.path[0]+"/cpAndStart.sh")
    app.run(port=8888)

#!/usr/bin/env python
# encoding: utf-8

# @Time         : 2018/3/14 下午3:04
# @Author       : zk
# @Mail         : zk1006@live.cn 
# @File         : shell.py
# @description  : shell命令执行控制器
import subprocess
import datetime


def exec_cmd(cmd):
    tmp = r'/tmp/deploy.tmp.log'
    log = r'/tmp/deploy.' + datetime.datetime.now().strftime('%Y-%m-%d') + '.log'
    f = open(tmp, "w")
    lf = open(log, "a+")
    lf.write(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f  ') + 'run:' + cmd)
    res = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    while True:
        data = res.stdout.readline()
        if data == b'':
            if res.poll() is not None:
                break
        else:
            log = res.stdout.readline().decode() + '\n'
            f.write(log)
            lf.write(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f  ') + log)
    f.close()
    lf.close()
#!/usr/bin/env python
# encoding: utf-8

# @Time         : 2018/3/15 上午11:28
# @Author       : zk
# @Mail         : zk1006@live.cn 
# @File         : settings.py
# @description  : 配置信息

DATABASES = {
    'NAME': 'bh-online-trade',
    'USER': 'root',
    'PASSWORD': '159256',
    'HOST': '192.168.1.6',
    'PORT': '3306'
}

RQ_QUEUES = {
    'HOST': '192.168.1.22',
    'PORT': 6379,
    'DB': 7,
    'PASSWORD': 'ylzf2018',
    'DEFAULT_TIMEOUT': 360
}
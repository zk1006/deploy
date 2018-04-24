#!/usr/bin/env python
# encoding: utf-8

# @Time         : 2018/4/23 下午5:21
# @Author       : zk
# @Mail         : zk1006@live.cn 
# @File         : menu.py
# @description  :


class Menu:
    def __init__(self, user, roles, url, name):
        self.user = user
        self.url = url
        self.name = name
        self.roles = roles
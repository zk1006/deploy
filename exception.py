#!/usr/bin/env python
# encoding: utf-8

# @Time         : 2018/4/23 下午4:48
# @Author       : zk
# @Mail         : zk1006@live.cn 
# @File         : exception.py
# @description  :


class DataEx(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)
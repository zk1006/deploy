#!/usr/bin/env python
# encoding: utf-8

# @Time         : 2018/3/16 下午3:07
# @Author       : zk
# @Mail         : zk1006@live.cn 
# @File         : model.py
# @description  :


class pro:
    def __init__(self, base_svn_path, pro_name, bak_path, pro):
        self.base_svn_path = base_svn_path
        self.pro_name = pro_name
        self.bak_path = bak_path
        self.pro = pro

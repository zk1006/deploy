#!/usr/bin/env python
# encoding: utf-8

# @Time         : 2018/3/16 下午3:07
# @Author       : zk
# @Mail         : zk1006@live.cn 
# @File         : model.py
# @description  :

import json


class pro:
    def __init__(self, base_svn_path, pro_name, bak_path, pro):
        self.base_svn_path = base_svn_path
        self.pro_name = pro_name
        self.bak_path = bak_path
        self.pro = pro


class pro_path:
    def __init__(self, svn_path, tomcat_path):
        self.svn_path = svn_path
        self.tomcat_path = tomcat_path


    def serialize_instance(obj):
        d = {'__classname__': type(obj).__name__}
        d.update(vars(obj))
        return d

#!/usr/bin/env python
# encoding: utf-8

# @Time         : 2018/3/15 上午11:06
# @Author       : zk
# @Mail         : zk1006@live.cn
# @File         : data.py
# @description  :

import pymysql
import redis
import settings


class DB:
    def __init__(self):
        prop = getattr(settings, 'DATABASES')
        self.DB_HOST = prop['HOST']
        self.DB_PORT = prop['PORT']
        self.DB_USER = prop['USER']
        self.DB_PWD = prop['PASSWORD']
        self.DB_NAME = prop['NAME']
        self.conn = self.getConnection()

    def getConnection(self):
        return pymysql.Connect(
            host=self.DB_HOST,  # 设置MYSQL地址
            port=self.DB_PORT,  # 设置端口号
            user=self.DB_USER,  # 设置用户名
            passwd=self.DB_PWD,  # 设置密码
            db=self.DB_NAME,  # 数据库名
            charset='utf8'  # 设置编码
        )

    def query(self, sqlString):
        cursor = self.conn.cursor()
        cursor.execute(sqlString)
        returnData = cursor.fetchall()
        cursor.close()
        self.conn.close()
        return returnData

    def update(self, sqlString):
        cursor = self.conn.cursor()
        cursor.execute(sqlString)
        self.conn.commit()
        cursor.close()
        self.conn.close()


class REDIS:
    def __init__(self):
        prop = getattr(settings,'RQ_QUEUES')
        self.DB_HOST = prop["HOST"]
        self.DB_PORT = prop["PORT"]
        self.DB_PWD = prop["PASSWORD"]
        self.DB_INDEX = prop["DB"]
        self.TIMEOUT = prop["DEFAULT_TIMEOUT"]
        self.conn = self.getConnection()

    def getConnection(self):
        return redis.Redis(
            host=self.DB_HOST,
            port=self.DB_PORT,
            db=self.DB_INDEX,
            password=self.DB_PWD,
            socket_timeout=self.TIMEOUT,
            connection_pool=None,
            errors='strict',
            decode_responses=True)

    def get(self, key):
        redis = self.conn
        return redis.get(key)

    def add(self, key,value):
        redis = self.conn
        return redis.set(key, value)

    def addex(self, key,value,extime):
        redis = self.conn
        return redis.set(key, value, ex=extime)


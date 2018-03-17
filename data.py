#!/usr/bin/env python
# encoding: utf-8

# @Time         : 2018/3/15 上午11:06
# @Author       : zk
# @Mail         : zk1006@live.cn
# @File         : data.py
# @description  : redis|mysql 连接类

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
        self.conn = self.get_connection()

    def get_connection(self):
        return pymysql.Connect(
            host=self.DB_HOST,
            port=self.DB_PORT,
            user=self.DB_USER,
            passwd=self.DB_PWD,
            db=self.DB_NAME,
            charset='utf8'
        )

    def query(self, sql_string):
        cursor = self.conn.cursor()
        cursor.execute(sql_string)
        return_data = cursor.fetchall()
        cursor.close()
        self.conn.close()
        return return_data

    def update(self, sql_string):
        cursor = self.conn.cursor()
        cursor.execute(sql_string)
        self.conn.commit()
        cursor.close()
        self.conn.close()


class REDIS:
    def __init__(self):
        prop = getattr(settings, 'RQ_QUEUES')
        self.DB_HOST = prop["HOST"]
        self.DB_PORT = prop["PORT"]
        self.DB_PWD = prop["PASSWORD"]
        self.DB_INDEX = prop["DB"]
        self.TIMEOUT = prop["DEFAULT_TIMEOUT"]
        self.conn = self.get_connection()

    def get_connection(self):
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
        conn = self.conn
        return conn.get(key)

    def add(self, key, value):
        conn = self.conn
        return conn.set(key, value)

    def add_ex(self, key, value, ex_time):
        conn = self.conn
        return conn.set(key, value, ex=ex_time)

    def get_keys(self):
        conn = self.conn
        return conn.keys()

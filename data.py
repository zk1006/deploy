#!/usr/bin/env python
# encoding: utf-8

# @Time         : 2018/3/15 上午11:06
# @Author       : zk
# @Mail         : zk1006@live.cn
# @File         : data.py
# @description  : redis|mysql 连接类

import redis
import settings
import mysql.connector
import exception as ex
# import time
# import random
# from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor


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
        return mysql.connector.connect(
            user=self.DB_USER,
            password=self.DB_PWD,
            port=self.DB_PORT,
            host=self.DB_HOST,
            database=self.DB_NAME)

    def query(self, sql_string):
        cursor = self.conn.cursor()
        try:
            cursor.execute(sql_string)
            return_data = cursor.fetchall()
        except mysql.connector.Error as e:
            print('query error!{}'.format(e))
        finally:
            cursor.close()
            self.conn.close()
        return return_data

    def update(self, sql_string):
        cursor = self.conn.cursor()
        try:
            cursor.execute(sql_string)
            self.conn.commit()
        except mysql.connector.Error as e:
            print('update error!{}'.format(e))
        finally:
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

    def __init__(self, index):
        if not isinstance(index, int) or -1 > index or index > 15:
            raise ex.DataEx('数据库索引超出范围')
        prop = getattr(settings, 'RQ_QUEUES')
        self.DB_HOST = prop["HOST"]
        self.DB_PORT = prop["PORT"]
        self.DB_PWD = prop["PASSWORD"]
        self.DB_INDEX = index
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
        conn = self.get_connection()
        return conn.get(key)

    def add(self, key, value):
        conn = self.get_connection()
        return conn.set(key, value)

    def add_ex(self, key, value, ex_time):
        conn = self.get_connection()
        return conn.set(key, value, ex=ex_time)

    def get_keys(self):
        conn = self.get_connection()
        return conn.keys()


# def randtime():
#     a1 = (2018,2,27,0,0,0,0,0,0)
#     a2 = (2018,3,28,23,59,59,0,0,0)
#     start = time.mktime(a1)    #生成开始时间戳
#     end = time.mktime(a2)      #生成结束时间戳
#
#     for i in range(10):
#         t = random.randint(start,end)    #在开始和结束时间戳中随机取出一个
#         date_touple = time.localtime(t)          #将时间戳生成时间元组
#         date = time.strftime('%Y-%m-%d %H:%M:%S', date_touple)  #将时间元组转成格式化字符串（1976-05-21）
#         return date

# def add(i):
#     datetime = randtime()
#     sqlstr = """insert into trade_order ( TIMEOUT, PAYER_FEE, CURRENCY, CLOSE_TIME, PAYER, CARD_TYPE, REDIRECT_URL,
#                      REFUND_AMOUNT, BUSINESS_TYPE, PAY_TYPE,BUSINESS_FLAG2, RECEIVER, COST, ORDER_TIME, VERSION, CLEARING_FINISH_TIME, PAID_AMOUNT,
#                      PAYER_ROLE, NOTIFY_URL, STATUS, BUSINESS_FLAG1, RECEIVER_ROLE, SUPPORT_REFUND_TYPE, SUCCESS_PAY_TIME,
#                      SUPPORT_REFUND_HANDLE_TYPE, CREATE_TIME, REFUND_STATUS, REQUEST_CODE, CODE, CLEARING_STATUS,
#                      PRODUCTS, RECEIVER_FEE, REFUNDABLE_AMOUNT, AMOUNT, REPEAT_FLAG)
#                      values ('{}', null, 'CNY', null, null, null, null, '0.00', 'SAILS', 'WXNATIVE', null, 'C100000', null,
#                      '{}', '4810953615962536', null, '0.00', 'UN_REGISTERED', 'http://www.baidu.com', 'WAIT_PAY',
#                      '', 'CUSTOMER', 'PART_REFUND', null, null,
#                      '{}', 'NOT_REFUND', '100426852603','TO{}', 'UN_CLEARING', null, null, null, '550.00', 'FALSE')"""
#     sqlstr = sqlstr.format(datetime, datetime, datetime, str(random.uniform(1, 15)))
#     DB().update(sqlstr)
#     print("执行完成:{}".format(i))

if __name__ == '__main__':
    print(REDIS(15))
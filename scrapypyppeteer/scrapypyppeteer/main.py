#!/usr/bin/env python
#-*- coding:utf-8 -*-

from scrapy.cmdline import execute
import os
import sys
import pymysql

#添加当前项目的绝对地址
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
#执行 scrapy 内置的函数方法execute，  使用 crawl 爬取并调试，最后一个参数jobbole 是我的爬虫文件名
execute(['scrapy', 'crawl', 'yiqing'])



# MYSQL_HOST = 'www.tianjinairlines.cn'
# MYSQL_DATABASE = 'yiqing'
# MYSQL_PORT = 15000
# MYSQL_USER = 'root'
# MYSQL_PASSWORD = 'f841184200'
# db = pymysql.connect(host= MYSQL_HOST, user= MYSQL_USER, password= MYSQL_PASSWORD, database= MYSQL_DATABASE, charset='utf8', port=MYSQL_PORT)
# cursor = db.cursor()
#
#
# item = {'a':'lala', 'b':'llab'}
# data = dict(item)
# keys = ', '.join(data.keys())
# values = ', '.join(['% s'] * len(data))
# sql = 'insert into % s (% s) values (% s)' % ('yiqing', keys, values)
# cursor.execute(sql, tuple(data.values()))
# db.commit()



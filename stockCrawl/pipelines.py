# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


import datetime
import mysql.connector as mariadb
from stockCrawl.items import CrawlItem

class SQLStorePipeline(object):

    def __init__(self):
       self.mariadb_connection = mariadb.connect(host= 'localhost', user= 'root', passwd= '', db= 'test', charset="utf8",
                           use_unicode=True)
       self.cursor = self.mariadb_connection.cursor()


    def process_item(self, item, spider):
        stock_id = self._get_id(item)
        self.cursor.execute(
            "INSERT INTO TABLE_STOCK_CODE(STOCK_CODE,STOCK_NAME,CREATE_DATE) VALUES (%s, %s, %s);",
            (item['stock_id'][0],
             item['stock_name'][0],
             datetime.datetime.now()
             ))
        self.mariadb_connection.commit()

    def _get_id(self, item):
        return item['stock_id'][0]
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from twisted.enterprise import adbapi
import datetime
import logging
import MySQLdb.cursors
from stockCrawl.items import CrawlItem
from scrapy.exceptions import DropItem

class SQLStorePipeline(object):
    def __init__(self):
        try:
            self.conn = MySQLdb.connect(user='root', passwd='', db='test', host='localhost', charset="utf8",
                                        use_unicode=True)
            # print("1")
            self.cursor = self.conn.cursor()
            # print("2")
        except MySQLdb.Error, e:
            print "Error %d: %s" % (e.args[0], e.args[1])
            # log data to json file

    def process_item(self, item, spider):
        # create record if doesn't exist.
        self.cursor.execute(
            "select * from TABLE_STOCK_CODE where STOCK_CODE = %s",
            (item['stock_id'][0].encode('utf-8')))
        result = self.cursor.fetchone()
        # print "select * from apt2u.apt where aptname = '%s' and link = 'http://www.apt2you.com/houseSaleDetailInfo.do?manageNo=%s' and company = '%s' and receiptdate = '%s' and result_date = '%s'" % (item['aptname'][0].encode('utf-8'), item['link'][0].encode('utf-8'), item['company'][0].encode('utf-8'), item['receiptdate'][0].encode('utf-8'), item['result_date'][0].encode('utf-8'))

        if result:
            print("data already exist")
        else:
            try:
                self.cursor.execute(
                    "insert into TABLE_STOCK_CODE(STOCK_CODE, STOCK_NAME, CREATE_DATE) values (%s, %s, %s)",
                    (item['stock_id'][0].encode('utf-8'),
                     item['stock_name'][0].encode('utf-8'),
                     datetime.datetime.now()))
                self.conn.commit()
            except MySQLdb.Error, e:
                print "Error %d: %s" % (e.args[0], e.args[1])
                return item

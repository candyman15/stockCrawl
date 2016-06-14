# -*- coding: utf-8 -*-

# Scrapy settings for stockCrawl project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html


BOT_NAME = 'stockCrawl'

SPIDER_MODULES = ['stockCrawl.spiders']
NEWSPIDER_MODULE = 'stockCrawl.spiders'
DEPTH_LIMIT = 1

ITEM_PIPELINES = {'stockCrawl.pipelines.SQLStorePipeline':300,}



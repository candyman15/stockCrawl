from scrapy.spider import Spider
from scrapy.selector import Selector
from stockCrawl.items import CrawlItem

class StockSpider(Spider):
    pipelines = ['stock']
    name = "stock"
    allowed_domains = ["finance.daum.net"]
    start_urls = [
        "http://finance.daum.net/quote/all.daum?type=S&stype=P",
        "http://finance.daum.net/quote/all.daum?type=S&stype=Q"
    ]

    def parse(self, response):
        hxs = Selector(response)

        sites = hxs.xpath('//table[@class="gTable clr"]')
        items = []

        for site in sites:
            item = CrawlItem()
            href = site.xpath('//td[@class="txt"]/a/@href').extract()
            item['stock_id'] = [i.split('=')[1] for i in href]
            item['stock_name'] = site.xpath('//td[@class="txt"]/a//text()').extract()
            items.append(item)

        return items
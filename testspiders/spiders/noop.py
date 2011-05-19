from scrapy.spider import BaseSpider

class NoopSpider(BaseSpider):
    name = "noop"

    def parse(self, response):
        pass

from scrapy.spider import Spider

class NoopSpider(Spider):
    name = "noop"

    def parse(self, response):
        pass

import scrapy


class NoopSpider(scrapy.Spider):
    name = "noop"

    def parse(self, response):
        pass

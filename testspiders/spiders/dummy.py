from scrapy.spider import BaseSpider

class DummySpider(BaseSpider):
    name = "dummy"
    allowed_domains = ["example.com", "iana.org"]
    start_urls = (
        'http://www.example.com/',
        )

    def parse(self, response):
        pass

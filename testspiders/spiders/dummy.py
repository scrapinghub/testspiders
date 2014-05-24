from scrapy.spider import Spider

class DummySpider(Spider):
    name = "dummy"
    allowed_domains = ["example.com", "iana.org"]
    start_urls = (
        'http://www.example.com/',
        )

    def parse(self, response):
        pass

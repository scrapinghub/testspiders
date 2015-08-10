import scrapy

class DummySpider(scrapy.Spider):
    name = "dummy"
    allowed_domains = ["example.com", "iana.org"]
    start_urls = (
        'http://www.example.com/',
        )

    def parse(self, response):
        pass

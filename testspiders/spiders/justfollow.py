import scrapy
from scrapy.http import TextResponse


class Spider(scrapy.Spider):

    name = 'justfollow'

    def start_requests(self):
        url = getattr(self, 'url', 'http://scrapinghub.com')
        yield scrapy.Request(url, dont_filter=True)

    def parse(self, response):
        if not isinstance(response, TextResponse):
            return

        if response.xpath('//form'):
            yield scrapy.FormRequest.from_response(response,
                                                   callback=self.parse)

        for href in response.xpath('//a/@href').extract():
            yield scrapy.Request(response.urljoin(href), self.parse)

# -*- coding: utf-8 -*-
import scrapy
import scrapy.contrib.spiders


class LxtestSpider(scrapy.contrib.spiders.CrawlSpider):
    name = 'lxtest'
    allowed_domains = ['example.com']
    start_urls = ['http://www.example.com/']

    rules = (
        scrapy.contrib.spiders.Rule(
            scrapy.contrib.linkextractors.LinkExtractor(allow=r'Items/'),
            callback='parse_item',
            follow=True,
        ),
    )

    def parse_item(self, response):
        return {}

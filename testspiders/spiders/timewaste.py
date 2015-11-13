import scrapy
from twisted.internet import reactor, defer


class Spider(scrapy.Spider):
    name = 'timewaste'
    start_urls = ('https://example.com',)

    def __init__(self, **kw):
        self.timeout = int(kw.pop('timeout', '600'))
        super(Spider, self).__init__(**kw)

    def parse(self, response):
        self.log('I will waste your time for {} seconds'.format(self.timeout))
        dfd = defer.Deferred()
        reactor.callLater(self.timeout, dfd.callback, None)
        return dfd

    def stop(self):
        self.crawler.engine.close_spider(self, 'timeout')

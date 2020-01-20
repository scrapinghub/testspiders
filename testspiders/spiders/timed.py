"""
Crawll-all spider without domain restriction
"""
from testspiders.spiders.followall import FollowAllSpider


class TimedSpider(FollowAllSpider):

    name = 'timed'
    url = None

    def __init__(self, **kw):
        self.timeout = int(kw.pop('timeout', '60'))
        super(TimedSpider, self).__init__(**kw)

    def start_requests(self):
        from twisted.internet import reactor
        reactor.callLater(self.timeout, self.stop)
        return super(TimedSpider, self).start_requests()

    def stop(self):
        self.crawler.engine.close_spider(self, 'timeout')

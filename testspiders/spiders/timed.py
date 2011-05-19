"""
Crawll-all spider without domain restriction
"""
from testspiders.spiders.followall import FollowAllSpider
from twisted.internet import reactor


class TimedSpider(FollowAllSpider):

    name = 'timed'
    url = None

    def __init__(self, url=None, timeout=60):
        super(TimedSpider, self).__init__(url)
        self.timeout = int(timeout)

    def start_requests(self):
        reactor.callLater(self.timeout, self.stop)
        return super(TimedSpider, self).start_requests()

    def stop(self):
        self.crawler.engine.close_spider(self, 'timeout')

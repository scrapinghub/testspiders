"""
Crawll-all spider without domain restriction
"""
from testspiders.spiders.followall import FollowAllSpider


class FollowAll3Spider(FollowAllSpider):

    name = 'followall3'
    url = None

    def __init__(self, *args, **kwargs):
        super(FollowAll3Spider, self).__init__(*args, **kwargs)
        self.allowed_domains = []

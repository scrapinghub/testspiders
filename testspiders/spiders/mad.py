"""
Spider that blocks, logs a warning and raises an error randomly
"""
import time
import random
from scrapy import log
from testspiders.spiders.followall import FollowAllSpider


class MadSpider(FollowAllSpider):

    name = 'mad'
    url = None
    timeout_choices = range(10)

    def _get_item(self, response):
        # simulate block call
        timeout = random.choice(self.timeout_choices)
        time.sleep(timeout)

        # simulate warnings and errors
        if timeout % 3:
            self.log("something happened", level=log.WARNING)
        else:
            raise Exception("something bad happened")

        return super(MadSpider, self)._get_item(response)


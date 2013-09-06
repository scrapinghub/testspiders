import random
from scrapy.exceptions import IgnoreRequest


class RandomUserAgent(object):
    """Randomly rotate user agents based on a list of predefined ones"""

    def __init__(self, agents):
        self.agents = agents

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings.getlist('USER_AGENTS'))

    def process_request(self, request, spider):
        request.headers.setdefault('User-Agent', random.choice(self.agents))


class ErrorMonkeyMiddleware(object):

    def process_request(self, request, spider):
        if 'x-ignore-request' in request.url:
            raise IgnoreRequest()
        elif 'x-error-request' in request.url:
            _ = 1 / 0

    def process_response(self, request, response, spider):
        if 'x-ignore-response' in request.url:
            raise IgnoreRequest()
        elif 'x-error-response' in request.url:
            _ = 1 / 0
        else:
            return response

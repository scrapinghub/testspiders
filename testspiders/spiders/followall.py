from urlparse import urlparse
from scrapy.http import Request, HtmlResponse
from scrapy.spider import BaseSpider
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from testspiders.items import Page

class FollowAllSpider(BaseSpider):

    name = 'followall'
    url = None

    def __init__(self, url=None):
        super(FollowAllSpider, self).__init__()
        if not url:
            raise RuntimeError("Missing spider argument: url")
        self.url = url
        self.allowed_domains = [urlparse(url).hostname.lstrip('www.')]
        self.link_extractor = SgmlLinkExtractor()
        self.cookies_seen = set()

    def start_requests(self):
        return [Request(self.url, callback=self.parse)]

    def parse(self, response):
        page = Page(url=response.url, size=len(response.body),
            referer=response.request.headers.get('Referer'))
        self._set_new_cookies(page, response)
        r = [page]
        if isinstance(response, HtmlResponse):
            links = self.link_extractor.extract_links(response)
            r += [Request(x.url, callback=self.parse) for x in links]
        return r

    def _set_new_cookies(self, page, response):
        cookies = []
        for cookie in [x.split(';', 1)[0] for x in response.headers.getlist('Set-Cookie')]:
            if cookie not in self.cookies_seen:
                self.cookies_seen.add(cookie)
                cookies.append(cookie)
        if cookies:
            page['newcookies'] = cookies

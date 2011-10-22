from urlparse import urlparse
from scrapy.http import Request, HtmlResponse
from scrapy.spider import BaseSpider
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from testspiders.items import Page

class FollowAllSpider(BaseSpider):

    name = 'followall'
    item_cls = Page

    def __init__(self, **kw):
        super(FollowAllSpider, self).__init__(**kw)
        if 'domain' in kw:
            self.url = 'http://%s/' % kw['domain']
        else:
            self.url = kw.get('url', 'http://scrapinghub.com')
        self.allowed_domains = [urlparse(self.url).hostname.lstrip('www.')]
        self.link_extractor = SgmlLinkExtractor()
        self.cookies_seen = set()

    def start_requests(self):
        return [Request(self.url, callback=self.parse)]

    def parse(self, response):
        page = self._get_item(response)
        r = [page]
        r.extend(self._extract_requests(response))
        return r

    def _get_item(self, response):
        item = self.item_cls(url=response.url, size=str(len(response.body)),
            referer=response.request.headers.get('Referer'))
        self._set_new_cookies(item, response)
        return item

    def _extract_requests(self, response):
        r = []
        if isinstance(response, HtmlResponse):
            links = self.link_extractor.extract_links(response)
            r.extend(Request(x.url, callback=self.parse) for x in links)
        return r

    def _set_new_cookies(self, page, response):
        cookies = []
        for cookie in [x.split(';', 1)[0] for x in response.headers.getlist('Set-Cookie')]:
            if cookie not in self.cookies_seen:
                self.cookies_seen.add(cookie)
                cookies.append(cookie)
        if cookies:
            page['newcookies'] = cookies

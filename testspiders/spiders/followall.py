from urlparse import urlparse
from scrapy.http import Request, HtmlResponse
from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from testspiders.items import Page

class FollowAllSpider(Spider):

    name = 'followall'

    def __init__(self, **kw):
        super(FollowAllSpider, self).__init__(**kw)
        url = kw.get('url') or kw.get('domain') or 'http://scrapinghub.com/'
        if not url.startswith('http://') and not url.startswith('https://'):
            url = 'http://%s/' % url
        self.url = url
        self.allowed_domains = [urlparse(url).hostname.lstrip('www.')]
        self.link_extractor = SgmlLinkExtractor()
        self.cookies_seen = set()

    def start_requests(self):
        return [Request(self.url, callback=self.parse)]

    def parse(self, response):
        """Parse a PageItem and all requests to follow

        @url http://www.scrapinghub.com/
        @returns items 1 1
        @returns requests 1
        @scrapes url title foo
        """
        page = self._get_item(response)
        r = [page]
        r.extend(self._extract_requests(response))
        return r

    def _get_item(self, response):
        item = Page(url=response.url, size=str(len(response.body)),
            referer=response.request.headers.get('Referer'))
        self._set_title(item, response)
        self._set_new_cookies(item, response)
        return item

    def _extract_requests(self, response):
        r = []
        if isinstance(response, HtmlResponse):
            links = self.link_extractor.extract_links(response)
            r.extend(Request(x.url, callback=self.parse) for x in links)
        return r

    def _set_title(self, page, response):
        if isinstance(response, HtmlResponse):
            title = Selector(response).xpath("//title/text()").extract()
            if title:
                page['title'] = title[0]

    def _set_new_cookies(self, page, response):
        cookies = []
        for cookie in [x.split(';', 1)[0] for x in response.headers.getlist('Set-Cookie')]:
            if cookie not in self.cookies_seen:
                self.cookies_seen.add(cookie)
                cookies.append(cookie)
        if cookies:
            page['newcookies'] = cookies

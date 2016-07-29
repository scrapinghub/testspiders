# coding: utf8

import scrapy

try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse


class BrokenLink(scrapy.Spider):
    """
    Spider arguments:
    - input_url: Where to start the crawl with.
    - allowed_domains (optional): Comma-separated list of domains to restrict the crawl with. If not specified, it would be inferred from the input URL, e.g. http://doc.scrapy.org/en/latest/intro/overview.html -> doc.scrapy.org

    Settings:
    - DEPTH_LIMIT: Controls the maximum depth (defaults to 50).
    - MAX_REQUESTS: Controls the maximum requests (defaults to 100000). The actual number of requests may be slightly different, e.g. MAX_REQUESTS=1000 and the spider stops when having sent 1008 requests.
    """
    name = 'broken_link'
    custom_settings = {
        'HTTPERROR_ALLOW_ALL': True,
        'DEPTH_LIMIT': 50,
        'MAX_REQUESTS': 100000,
        'RETRY_HTTP_CODES': [],
    }

    def __init__(self, input_url, allowed_domains=None, *args, **kwargs):
        """Initializes the instance"""
        super(BrokenLink, self).__init__(*args, **kwargs)
        self.start_urls = [input_url]
        if allowed_domains:
            self.allowed_domains = allowed_domains.split(',')
        else:
            netloc = urlparse(input_url).netloc
            domain = netloc.split('@')[-1].split(':')[0]
            self.allowed_domains = [domain]

    def start_requests(self):
        """Generates initial requests"""
        for url in self.start_urls:
            # Explicitly set the errback handler
            yield scrapy.Request(
                url,
                dont_filter=True,
                callback=self.parse,
                errback=self.errback
            )

    def parse(self, response):
        """Parses a default response"""
        if not isinstance(response, scrapy.http.TextResponse):
            self.crawler.stats.inc_value('non_text_response')
            return
        if response.status >= 400 and response.status <= 599:
            yield {
                'url': response.url,
                'status': 'invalid_http_status',
                'http_status': response.status,
            }
        max_reqs = self.settings.getint('MAX_REQUESTS', 0)
        stats = self.crawler.stats
        for href in response.css('a::attr(href)').extract():
            if max_reqs and max_reqs < stats.get_value('scheduler/enqueued'):
                break
            yield scrapy.Request(
                response.urljoin(href),
                callback=self.parse,
                errback=self.errback
            )

    def errback(self, err):
        """Handles an error"""
        return {
            'url': err.request.url,
            'status': 'error_downloading_http_response',
            'message': str(err.value),
        }

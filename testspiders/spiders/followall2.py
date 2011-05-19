from scrapy.item import Field
from scrapy.selector import HtmlXPathSelector

from testspiders.items import Page
from testspiders.spiders.followall import FollowAllSpider


class Page2(Page):
    title = Field()
    dom_nodes = Field()
    dom_tables = Field()
    scripts = Field()
    headers = Field()


class FollowAll2Spider(FollowAllSpider):

    name = 'followall2'
    url = None
    item_cls = Page2

    def _get_item(self, response):
        item = super(FollowAll2Spider, self)._get_item(response)
        hxs = HtmlXPathSelector(response)
        try:
            item['title'] = hxs.select('//title[1]/text()').extract()[0]
        except IndexError:
            pass
        item['dom_nodes'] = hxs.select('count(//*)').extract()[0]
        item['dom_tables'] = hxs.select('count(//table)').extract()[0]
        item['scripts'] = hxs.select('//script/@src').extract()
        item['headers'] = response.headers.copy()
        return item

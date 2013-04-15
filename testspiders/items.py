from scrapy.item import Item, Field

class Page(Item):
    url = Field()
    title = Field()
    size = Field()
    referer = Field()
    newcookies = Field()
    body = Field()


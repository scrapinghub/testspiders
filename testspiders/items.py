from scrapy.item import Item, Field

class Page(Item):
    url = Field()
    size = Field()
    referer = Field()
    newcookies = Field()


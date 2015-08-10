import logging
import tempfile
import scrapy
from testspiders.items import Page


LOREMIPSUM = b'''\
Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed
diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat
volutpat. Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper
suscipit lobortis nisl ut aliquip ex ea commodo consequat. Duis autem vel eum
iriure dolor in hendrerit in vulputate velit esse molestie consequat, vel illum
dolore eu feugiat nulla facilisis at vero eros et accumsan et iusto odio
dignissim qui blandit praesent luptatum zzril delenit augue duis dolore te
feugait nulla facilisi. Nam liber tempor cum soluta nobis eleifend option
congue nihil imperdiet doming id quod mazim placerat facer possim assum. Typi
non habent claritatem insitam; est usus legentis in iis qui facit eorum
claritatem. Investigationes demonstraverunt lectores legere me lius quod ii
legunt saepius. Claritas est etiam processus dynamicus, qui sequitur mutationem
consuetudium lectorum. Mirum est notare quam littera gothica, quam nunc putamus
parum claram, anteposuerit litterarum formas humanitatis per seacula quarta
decima et quinta decima. Eodem modo typi, qui nunc nobis videntur parum clari,
fiant sollemnes in futurum.'''


class LoremipsumSpider(scrapy.Spider):
    name = "loremipsum"
    loremfile = None

    def start_requests(self):
        self.loremfile = tempfile.NamedTemporaryFile()
        self.loremfile.write(LOREMIPSUM)
        yield scrapy.Request('file://{0}'.format(self.loremfile.name))

    def parse(self, response):
        """Extract lorem ipsum text

        @url http://es.lipsum.com/
        @returns items 1 1
        @scrapes url title body
        """
        self.log(LOREMIPSUM[:30], level=logging.DEBUG)
        self.log(LOREMIPSUM[30:60], level=logging.INFO)
        self.log(LOREMIPSUM[60:90], level=logging.WARNING)
        self.log(LOREMIPSUM[90:120], level=logging.ERROR)
        yield Page(url=response.url, title=LOREMIPSUM[:20], body=LOREMIPSUM)
        if self.loremfile:
            url = 'file://{0}?x-error-response'.format(self.loremfile.name)
            yield scrapy.Request(url, callback=self.parse, errback=self.recover)

    def recover(self, failure):
        raise ValueError('hoho')

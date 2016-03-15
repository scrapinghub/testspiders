# testspiders

Useful test spiders for Scrapy http://scrapy.org

## Spiders

### brokenlink

Detects broken links of a given website.

Sample usage:
`scrapy crawl broken_link -a input_url=http://httpstat.us/`

Spider arguments:
- `input_url`: Where to start the crawl with.
- `allowed_domains` (optional): Comma-separated list of domains to restrict the crawl with. If not specified, it would be inferred from the input URL, e.g. https://intranet.scrapinghub.com/issues/57161 -> intranet.scrapinghub.com

Settings:
- `DEPTH_LIMIT`: Controls the maximum depth (defaults to 50).
- `MAX_REQUESTS`: Controls the maximum requests (defaults to 100000). The actual number of requests may be slightly different, e.g. MAX_REQUESTS=1000 and the spider stops when having sent 1008 requests.

### dummy

### followall

### justfollow

### localinfo

### loremipsum

### mad

### noop

### timed

### timewaste

# Scrapy settings for testspiders project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'testspiders'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['testspiders.spiders']
NEWSPIDER_MODULE = 'testspiders.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

# some sane limits by default (override if needed)
CLOSESPIDER_PAGECOUNT = 1000
CLOSESPIDER_TIMEOUT = 3600

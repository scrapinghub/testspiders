import os
import sys
import tempfile
import platform

import twisted
import OpenSSL
import lxml.etree
import scrapy


class LocalInfo(scrapy.Spider):
    name = 'localinfo'
    start_urls = 'https://example.com',

    def parse(self, response):
        item = {
            '__file__': __file__,
            '__name__': __name__,
            'cwd': os.path.abspath(os.path.curdir),
            'tmpdir': tempfile.gettempdir(),
        }
        item['versions'] = _versions()
        item['environ'] = os.environ.copy()
        return item


def _versions():
    lxml_version = ".".join(map(str, lxml.etree.LXML_VERSION))
    libxml2_version = ".".join(map(str, lxml.etree.LIBXML_VERSION))
    return {
        "Scrapy": scrapy.__version__,
        "lxml": lxml_version,
        "libxml2": libxml2_version,
        "Twisted": twisted.version.short(),
        "Python": sys.version.replace("\n", "- "),
        "pyOpenSSL": _get_openssl_version(),
        "Platform": platform.platform(),
    }


def _get_openssl_version():
    try:
        openssl = OpenSSL.SSL.SSLeay_version(OpenSSL.SSL.SSLEAY_VERSION)\
            .decode('ascii', errors='replace')
    # pyOpenSSL 0.12 does not expose openssl version
    except AttributeError:
        openssl = 'Unknown OpenSSL version'

    return '{} ({})'.format(OpenSSL.version.__version__, openssl)

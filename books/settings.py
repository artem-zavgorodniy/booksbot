# -*- coding: utf-8 -*-

BOT_NAME = 'books'

SPIDER_MODULES = ['books.spiders']
NEWSPIDER_MODULE = 'books.spiders'

ROBOTSTXT_OBEY = True
HTTPCACHE_ENABLED = True

DOWNLOADER_MIDDLEWARES = {'books.ZyteSmartProxyMiddleware': 610}
ZYTE_SMARTPROXY_ENABLED = True
ZYTE_SMARTPROXY_APIKEY = '05104e83eb2f4949a98ddfbbbeb90326'
ZYTE_SMARTPROXY_URL = 'https://proxy.crawlera.com:8011'
# -*- coding: utf-8 -*-
from urllib.parse import quote_plus
from scraper.lib.user_agent import get_user_agent

BOT_NAME = "scraper"

SPIDER_MODULES = ["scraper.spiders"]

NEWSPIDER_MODULE = "scraper.spiders"

ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)

# CONCURRENT_REQUESTS = 1

# settings.py
CONCURRENT_REQUESTS_PER_DOMAIN = 16
CONCURRENT_REQUESTS = 120  # Adjust the value based on your requirements
# settings.py
# HTTPCACHE_ENABLED = True
# settings.py
# AUTOTHROTTLE_ENABLED = True

CONCURRENT_REQUESTS_PER_IP = 16


# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# # Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = True

# # Override the default request headers:

# DEFAULT_REQUEST_HEADERS = {
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#     'Accept-Language': 'en',
# }
# LOG_ENABLED = False



ITEM_PIPELINES = {
    'scraper.pipelines.jobPipeline': 300,
}




# RETRY_TIMES = 3

# FEED_EXPORT_ENCODING = 'utf-8'

# DOWNLOAD_DELAY = 0

# DOWNLOAD_TIMEOUT = 30

# RANDOMIZE_DOWNLOAD_DELAY = True

# REACTOR_THREADPOOL_MAXSIZE = 128

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 1
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 0.25
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 128
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = True
# RETRY_ENABLED = True

# Retry on most error codes since proxies fail for different reasons
# RETRY_HTTP_CODES = [500, 502, 503, 504, 400, 401, 404, 405, 406, 407, 408, 409, 410, 429, 403]
# 
# PROXY_LIST = get_proxy()

# USER_AGENT = get_user_agent('random')

# DOWNLOADER_MIDDLEWARES = {
#     'scraper.middlewares.CrawlerSpiderMiddleware': 400,
#     'scraper.middlewares.RandomUserAgentMiddleware': 120,
#     'scrapy.spidermiddlewares.referer.RefererMiddleware': 80,
#     'scrapy.downloadermiddlewares.retry.RetryMiddleware': 90,
#     'scrapy.downloadermiddlewares.cookies.CookiesMiddleware': 130,
#     'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
#     'scrapy.downloadermiddlewares.redirect.RedirectMiddleware': 900,
# }
# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"

# FEED_EXPORT_ENCODING = "utf-8"
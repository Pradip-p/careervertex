# -*- coding: utf-8 -*-
from urllib.parse import quote_plus
from scraper.lib.user_agent import get_user_agent

BOT_NAME = "scraper"

SPIDER_MODULES = ["scraper.spiders"]

NEWSPIDER_MODULE = "scraper.spiders"

ROBOTSTXT_OBEY = False

# settings.py
CONCURRENT_REQUESTS_PER_DOMAIN = 16
CONCURRENT_REQUESTS = 120  # Adjust the value based on your requirements


CONCURRENT_REQUESTS_PER_IP = 16



ITEM_PIPELINES = {
    'scraper.pipelines.jobPipeline': 300,
}


# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"


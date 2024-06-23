from celery import shared_task
from scrapy import cmdline

@shared_task
def run_scrapy_spider():
    # Your code to run the Scrapy spider
    print("Running Scrapy Spider")
    # Add your Scrapy spider execution code here
    
# @shared_task
# def run_scrapy_spider():
    
    # cmdline.execute("scrapy crawl jobsnepal".split())

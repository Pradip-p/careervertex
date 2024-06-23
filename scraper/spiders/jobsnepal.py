# -*- coding: utf-8 -*-
from scrapy import Request, Spider
from scrapy import Request


class LinkedinSpider(Spider):
    
    name = 'jobsnepal'
    
    allowed_domains = ['jobsnepal.com']
    
    custom_settings = {
        'DOWNLOAD_DELAY': 2,
        'CONCURRENT_REQUESTS': 1,
        'ROBOTSTXT_OBEY': False,
        'LOG_LEVEL': 'DEBUG',
        'LOG_ENABLED': True,
        'ITEM_PIPELINES' : {
        'scraper.pipelines.jobPipeline': 300,
        }
    } 
    def start_requests(self):
        for page in range(1,2):
            url = f'https://www.jobsnepal.com/category/ngo-ingo-jobs?page={page}'
            yield Request(url,callback=self.parse, dont_filter=True)

    def parse(self, response):        
        urls = response.xpath('//div[@class="card-body"]/h2[@class="job-title"]/a/@href').extract()
        for url in urls:
            yield  Request(url, callback=self.parse_detail, dont_filter=True)
    
    def parse_detail(self, response):
        company_logo_url = response.xpath('//div[@class="company-logo mr-5"]/img/@src').extract_first()
        job_expiry_date = response.xpath('//div[@class="company-info"]/span[@class="job-expiry-date"]/text()').extract_first()   
        company_name = response.xpath('//h2[@class="company-title font-sans"]/text()').extract_first().strip()
        description_content = response.xpath('//span[@itemprop="description"]').getall()
        content = ' '.join(description_content)
        job_title = response.xpath('//div[@class="job-details"]/h1[@class="job-title pb-1 font-sans"]/text()').extract_first().strip()
        company_description = response.xpath('//p[@class="company-description text-justify"]/text()').extract_first()
        location = response.xpath('//td[@itemprop="address"]//span[@itemprop="addressLocality"]/text()').extract_first()
        apply_deadline = response.xpath('//div[@class="job-post-date-info mb-4"]//meta[@itemprop="validThrough"]/@content').extract_first()

        date_posted = response.xpath('//div[@class="job-post-date-info mb-4"]//meta[@itemprop="datePosted"]/@content').extract_first()
        employment_type = response.xpath('//td[@itemprop="employmentType"]//span[@class="font-weight-semibold"]/text()').extract_first()

        yield {
            'job_title': job_title,
            'logo_url': company_logo_url,
            'job_expiry_date': job_expiry_date,
            'company_name': company_name,
            'content': content,
            'scrape_link': response.url,
            'company_description':company_description,
            'location': location,
            'last_date':apply_deadline,
            'type': employment_type
        } 
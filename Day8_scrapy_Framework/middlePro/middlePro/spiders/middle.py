import scrapy


class MiddleSpider(scrapy.Spider):
    name = 'middle'
    allowed_domains = ['www.xx.com']
    start_urls = ['http://www.xx.com/']

    def parse(self, response):
        pass

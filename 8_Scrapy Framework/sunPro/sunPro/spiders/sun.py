import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class SunSpider(CrawlSpider):
    name = 'sun'
    # allowed_domains = ['www.xx.com']
    start_urls = ['http://news.sun0769.com/head/default_1.shtml']

    # 链接提取器：从start_url中根据指定规则进行指定文件的提取
    link = LinkExtractor(allow=r'page=\d+&ka=page-\d+')

    rules = (
        # 规则解析器：将链接提取器提取到的链接进行指定规则（callback）的解析操作
        # follow=True: 可以将链接提取器，继续作用到其提取到的链接，所对应的页面中。
        Rule(link, callback='parse_item', follow=True),


    )
    #解析新闻标号和标题
    def parse_item(self, response):
        #item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        print(response)

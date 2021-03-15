import scrapy


class FirstspiderSpider(scrapy.Spider):
    #爬虫文件的名称： 就是爬虫源文件的唯一标识
    name = 'firstSpider'

    #允许的域名:用来限定start_urls中那些可用
    #allowed_domains = ['www.google.com']

    #起始的url列表：该列表中存放的url会被scrapy自动进行请求的发送。
    start_urls = ['http://www.google.com/',
                  'http://www.baidu.com/']

    #用作于数据解析： response参数表示请求成功后响应对象
    def parse(self, response):
        print('result: ', response)

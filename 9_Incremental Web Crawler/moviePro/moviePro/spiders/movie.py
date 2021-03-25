# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from redis import Redis
from moviePro.items import MovieproItem
from scrapy_redis.spiders import RedisCrawlSpider


class MovieSpider(RedisCrawlSpider):
    name = 'movie'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.4567tv.tv/frim/index7.html']

    rules = (
        Rule(LinkExtractor(allow=r'/frim/index7-\d+\.html'), callback='parse_item', follow=True),
    )
    # 创建redis链接对象
    conn = Redis(host='127.0.0.1', port=6379)

    def parse_item(self, response):
        li_list = response.xpath('/html/body/div[1]/div/div/div/div[2]/ul/li')
        for li in li_list:
            # 获取详情页的url
            print(li)
            detail_url = 'http://www.4567tv.tv' + li.xpath('./div/div/h4/a/@herf').extract_first()
            # 将详情页的url存入redis的set中
            ex = self.conn.sadd('urls', detail_url)
            if ex == 1:
                print('该url没有被爬取过，可以进行数据的爬取')
                yield scrapy.Request(url=detail_url, callback=self.parst_detail)
            else:
                print('数据还没有更新，暂无新数据可爬取！')

    # 解析详情页中的电影名称和类型，进行持久化存储
    def parst_detail(self, response):
        item = MovieproItem()
        item['name'] = response.xpath('/html/body/div[1]/div/div/div/div[2]/h1/text()').extract_first()
        # item['describe'] = response.xpath('/html/body/div[1]/div/div/div/div[2]/p[5]/span[3]/text()').extract_first()
        # item['describe'] = ''.join(item['describe'])
        yield item


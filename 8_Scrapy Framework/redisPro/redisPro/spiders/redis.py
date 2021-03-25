import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
# import package of RedisCrawlSpider
from scrapy_redis.spiders import RedisCrawlSpider

from redisPro.items import RedisproItem


class RedisSpider(RedisCrawlSpider):#修改父类为RedisCrawlSpider
    name = 'redis'
    # allowed_domains = ['www.xx.com']
    # start_urls = ['http://www.xx.com/']

    redis_key = 'redis'

    rules = (
        Rule(LinkExtractor(allow=r'/archives/p\d+.html'), follow=True),
        Rule(LinkExtractor(allow=r'/archives/\d+'), callback="parse_item", follow=False)
    )

    def parse_item(self, response):
        title_list = response.xpath("//h1[@class='lyw-article-title-inner']//text()").getall()
        title = "".join(title_list[2]).strip()
        pub_time = "".join(title_list[1]).strip()
        item = RedisproItem()
        item['title'] = title
        item['pub_time'] = pub_time

        yield item

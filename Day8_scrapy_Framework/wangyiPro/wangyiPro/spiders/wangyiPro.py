import scrapy


class WangyiproSpider(scrapy.Spider):
    name = 'wangyiPro'
    #allowed_domains = ['www.x.com']
    start_urls = ['https://news.163.com/']
    models_urls = []#五大板块url
    #解析五大板块url
    def parse(self, response):
        li_list = response.xpath('//*[@id="index2016_wrap"]/div[1]/div[2]/div[2]/div[2]/div[2]/div/ul')
        alist = [3,4,6,7,8]
        for index in alist:
            model_url = li_list[index].xpath = ('./a/@href').extract_first()
            self.models_urls.append(model_url)
        #依次对每一个板块页面发送请求
        for url in self.models_urls:
            yield scrapy.Request(url,callback=self.parse_model)

    #
    def parse_model(self,response):
        pass




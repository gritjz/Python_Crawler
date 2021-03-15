import scrapy


class QiubaiSpider(scrapy.Spider):
    name = 'qiubai'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.qiushibaike.com/text/']

    def parse(self, response):
        #解析：作者名称和段子的内容
        div_list = response.xpath('//*[@class="content-block clearfix"]/div[2]/div')
        for div in div_list:
            #xpath返回的是列表，但是列表元素一定是selector类型对象
            #extract()可以将selector对象中data参数存储的字符串提取出来
            author = div.xpath('./div[1]/a[2]/h2/text()')[0].extract()
            #列表调用了.extract()之后，则表示将列表中每一个selector对象中data对应的字符串提取出来
            content = div.xpath('./a[1]/div/span//text()').extract()
            content = ''.join(content)
            print (author, content)

            break

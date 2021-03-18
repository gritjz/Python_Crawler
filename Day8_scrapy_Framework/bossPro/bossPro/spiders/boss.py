import scrapy


class BossSpider(scrapy.Spider):
    name = 'boss'
    # allowed_domains = ['www.xxx.com']
    start_urls = [
        'https://www.zhipin.com/job_detail/?query=python&city=100010000&industry=&position=']

    def parse(self, response):
        count = 0
        li_list = response.xpath('//*[@id="main"]/div/div[3]/ul/li')

        for li in li_list:
            job_name = li.xpath('./div/div[1]/div[1]/div/div[1]/span[1]/text()').extract()
            count += 1
            print(count)
            print(job_name)
            detail_url = 'https://www.zhipin.com' + li.xpath('./div/div[1]/div[1]/div/div[1]/span[1]/a/@href').extract()

            # 获取detail page的数据
            # 手动请求的发送
            yield scrapy.Request(detail_url, callback=self.parse_detail)

    def parse_detail(self, response):
        job_desc = response.xpath('//*[@id="main"]/div[3]/div/div[2]/div[2]/div[1]/div//text()').extract()
        job_desc = ''.join(job_desc)
        print(job_desc)

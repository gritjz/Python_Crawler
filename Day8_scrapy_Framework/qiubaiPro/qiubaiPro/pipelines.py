# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class QiubaiproPipeline:
    fp = None
    #重写父类的方法： 该方法旨在开始爬虫的时候被调用一次
    def open_spider(self,spider):
        print('开始爬虫......')
        self.fp = open('./qiubai.txt', 'w', encoding='utf-8')

    #专门用来处理item对象
    #该方法可以接受爬虫文件提交过来的item对象，见参数item
    #该方法每当yield接收到一个item就会被调用一次
    def process_item(self, item, spider):
        author = item['author']
        content = item['content']

        self.fp.write(author+': '+content+'\n')

        return item

    def close_spider(self,spider):
        print('FINISH SPIDER！')
        self.fp.close()
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import pymysql

class QiubaiproPipeline:
    fp = None

    # 重写父类的方法： 该方法旨在开始爬虫的时候被调用一次
    def open_spider(self, spider):
        print('START SPIDER......')
        self.fp = open('./qiubai.txt', 'w', encoding='utf-8')

    # 专门用来处理item对象
    # 该方法可以接受爬虫文件提交过来的item对象，见参数item
    # 该方法每当yield接收到一个item就会被调用一次
    def process_item(self, item, spider):
        author = item['author']
        content = item['content']
        self.fp.write(author + ':' + content)
        return item

    def close_spider(self, spider):
        self.fp.close()
        print('FINISH SPIDER！')

#pipeline文件中, 一个类对应将一组数据存储到一个平台或者载体中
class mysqlPipeLine(object):
    conn = None
    cursor = None
    def open_spider(self, spider):
        self.conn = pymysql.Connect(host='127.0.0.1',
                                    port=3306,
                                    user='root',
                                    password='123456',
                                    db='qiubai')

    def process_item(self, item, spider):
        self.cursor = self.conn.cursor()
        try:
            self.cursor.execute('insert into qiubai values("%s","%s")%(item["author"],item["content"])')
        except Exception as e:
            print(e)
            self.conn.rollback()

















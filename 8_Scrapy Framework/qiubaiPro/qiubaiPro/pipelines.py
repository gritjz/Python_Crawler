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
        # 只要return的item都会传递给下一个即将执行的pipeline，即使只有一个pipeline,可以不写但最好写上，为之后的代码提供方便
        return item

    def close_spider(self, spider):
        self.fp.close()
        print('FINISH SPIDER！')


# pipeline文件中, 一个类对应将一组数据存储到一个平台或者载体中
class mysqlPipeLine(object):
    conn = None
    cursor = None

    def open_spider(self, spider):
        print('START SPIDER2......')
        self.conn = pymysql.Connect(host='127.0.0.1',
                                    port=3306,
                                    user='root',
                                    password='zjn19900811',
                                    db='dbfortest',
                                    charset='utf8')

    def process_item(self, item, spider):
        sql = 'INSERT INTO ss VALUES("%s","%s")' % (item["author"], item["content"])
        self.cursor = self.conn.cursor()
        try:
            author = item["author"]
            content = item["content"]
            print(author+': '+ content)
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()
        print('FINISH SPIDER2！')

# 爬虫文件提交的item类型的对象最终先会提交给 优先级较高的pipeline

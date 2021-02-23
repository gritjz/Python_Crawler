# -*- coding:utf-8 -*-

from lxml import etree
if __name__ == '__main__':
    #实例化好了一个etree对象，且将被解析的源码加载到了对象中

    tree = etree.parse('test.html', etree.HTMLParser())

    #res = tree.xpath('/html/head/title')
    #res = tree.xpath('/html//title')
    #res = tree.xpath('//title')
    # res = tree.xpath('//div[@class="D1"]/p')#class = D1的div中的所有p标签
    #res = tree.xpath('//div[@class="D1"]/p[2]')  # class = D1的div中的第二个p标签,索引从1开始
    # res = tree.xpath('//div[@class="D3"]//li[3]/a/text()')[0]  # class = D3的div中的第三个li标签的a标签的文本
    res = tree.xpath('//div[@class="D2"]/img/@src')[0]

    print(res)

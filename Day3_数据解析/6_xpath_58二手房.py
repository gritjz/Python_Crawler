# -*- coding:utf-8 -*-
import requests
from lxml import etree
if __name__ == '__main__':
    #爬取页面源码数据
    url='https://bj.58.com/ershoufang/'
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
    }

    page_text = requests.get(url=url, headers=headers).text

    #数据解析
    tree = etree.HTML(page_text)

    fp = open('6_58ershou.txt','w', encoding='utf-8')
    #找到所有房源信息的div
    div_list = tree.xpath('//*[@id="__layout"]/div/section/section[3]/section[1]/section[2]/div')
    #解析每个房源的title
    for div in div_list:
        title = div.xpath('./a/div[2]/div[1]/div[1]/h3/text()')[0]#开头的点一定要有，表明从当前div开始
        fp.write(title+'\n')
        print(title)
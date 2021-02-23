# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
if __name__ == '__main__':
    #将本地Html文档加载进对象
    fp = open('./text.html', 'r', encoding='utf-8')
    soup = BeautifulSoup(fp,'lxml')
    print (soup.title.text) #soup."tag名字"返回文档中第一次tag出现的标签

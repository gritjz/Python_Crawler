# -*- coding:utf-8 -*-
import requests
from lxml import etree
import os

if __name__ == '__main__':
    # 爬取页面源码数据
    url = 'http://pic.netbian.com/4kmeinv'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
    }
    response = requests.get(url=url, headers=headers)

    page_text = response.text
    tree = etree.HTML(page_text)
    # 解析图片：src属性值 alt属性值
    li_list = tree.xpath('//*[@id="main"]/div[3]/ul/li')

    if not os.path.exists('./7_piclibs'):
        os.mkdir('./7_piclibs')
    for li in li_list:
        src = "http://pic.netbian.com" + li.xpath('./a/img/@src')[0]

        alt = li.xpath('./a/img/@alt')[0] + '.jpg'
        #通用处理中文乱码的解决方案
        alt = alt.encode('iso-8859-1').decode('gbk')
        # print(src, alt)
        img_data = requests.get(url=src,headers=headers).content
        img_path = './7_piclibs/'+alt
        with open(img_path,'wb') as fp:
            fp.write(img_data)
            print(src,'下载成功！！！')

# -*- coding:utf-8 -*-
#需求：爬取糗事百科中糗图板块下所有的糗图图片

import requests
import re
import os
if __name__ == '__main__':
    #创建一个文件夹保存所有图片
    if not os.path.exists('./1_qiutuLabs'):
        print('Hello')
        os.mkdir('./1_qiutuLabs')

    url='https://www.qiushibaike.com/imgrank/'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
    }
    #使用通用爬虫对一整张页面进行爬取
    page_text = requests.get(url=url, headers=headers).text
    #使用聚焦爬虫将页面中所有的糗图进行解析/提取, re.S单行匹配， re.M多行匹配
    ex = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'
    img_src_list = re.findall(ex, page_text, re.S)

    for src in img_src_list:
        #拼接完整图片地址
        src = 'https:' + src
        img_data = requests.get(url=src, headers=headers).content
        #生成图片名称，由地址截取
        img_name = src.split('/')[-1]
        #图片存储路径
        img_path= './1_qiutuLabs/'+img_name
        with open(img_path, 'wb') as fp:
            fp.write(img_data)
            print(img_name, '下载成功')
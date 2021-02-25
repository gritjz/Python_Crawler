# -*- coding:utf-8 -*-
import requests
from lxml import etree
import os

if __name__ == '__main__':
    # 爬取页面源码数据
    urls = {
        'https://www.shuzhiduo.com/A/kPzOE3OQ5x/',
        'https://crawler-test.com/',
        'https://www.qq.com/',
        'https://www.sina.com.cn/'
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
    }

    def get_content(url):
        print('Crawling ', url)
        #get method is a block method, get content 1 By 1.
        response = requests.get(url=url, headers=headers)
        if response.status_code == 200 :
            return response.content

    def parse_content(content):
        print('Data Length: ', len(content))

    for url in urls:
        content= get_content(url)
        parse_content(content)







# -*- coding:utf-8 -*-
# 需求：爬取三国演义所有章节标题和内容

import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
    }

    # 将首页页面数据进行爬取
    url = 'https://www.shicimingju.com/book/sanguoyanyi.html'
    res = requests.get(url=url, headers=headers).content
    page_text = str(res,'utf-8')

    # 在首页中解析标题和详情页url
    # 1.实例化BS对象
    soup = BeautifulSoup(page_text,'lxml')
    # 解析章节标题和详情页url
    li_list = soup.select('.book-mulu > ul > li')
    fp = open('./04_sanguo.txt', 'w', encoding='utf-8')

    for li in li_list:
        title = li.a.string
        detail_url = 'https://www.shicimingju.com/' + li.a['href']
        # 对详情页发请求获得章节内容
        res2 = requests.get(url=detail_url, headers=headers).content
        detail_page_text = str(res2,'utf-8')

        # 解析出详情页中相关章节内容
        detail_soup = BeautifulSoup(detail_page_text, 'lxml')
        content_tag = detail_soup.find('div', class_='chapter_content')
        content = content_tag.text

        fp.write(title + ': ' + content + '\n')
        print(title, '爬取成功！')

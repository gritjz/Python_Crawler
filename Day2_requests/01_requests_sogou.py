# 需求： 爬取搜狗首页
# -*- coding:utf-8 -*-


import requests


if __name__ == '__main__':
    # 1指定url
    url = 'https://www.sogou.com/'

    # 2发起请求
    # get()会返回一个响应对象
    response = requests.get(url=url)

    # 3获取响应数据
    page_text = response.text
    print(page_text)

    # 4持久化存储
    with open('./Result01_sogou.html', 'w', encoding='utf-8') as fp:
        fp.write(page_text)
    print('Finished')

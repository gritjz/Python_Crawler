# -*- coding:utf-8 -*-
import requests
from lxml import etree
import os

if __name__ == '__main__':
    # 爬取页面源码数据
    # url = 'https://www.aqistudy.cn/historydata/'
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
    # }
    #
    # page_text = requests.get(url=url,headers=headers).text
    #
    # tree = etree.HTML(page_text)
    # all_city_name = []
    # #热门城市名称
    # hot_li_list = tree.xpath('//div[@class="bottom"]/ul/li')
    # for hot_li in hot_li_list:
    #     hot_name = hot_li.xpath('./a/text()')[0]
    #     all_city_name.append(hot_name)
    # #全部城市名称
    # city_names_list = tree.xpath('//div[@class="bottom"]/ul/div[2]/li')
    # for li in city_names_list:
    #     city_name = li.xpath('./a/text()')[0]
    #     all_city_name.append(city_name)
    # all_city_name = list(set(all_city_name))
    # print(all_city_name)
    # print ('Total: '+str(len(all_city_name)))
#------------------------------------------------------------------------------------------------------------------------------------------------------
    #尝试使用同一个xpath定位热门和全部城市
    url = 'https://www.aqistudy.cn/historydata/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
    }
    page_text = requests.get(url=url, headers=headers).text
    tree = etree.HTML(page_text)
    all_city_name = []
    #热门：//div[@class="bottom"]/ul/li
    #全部：//div[@class="bottom"]/ul/div[2]/li
    #使用：| 或
    a_list = tree.xpath('//div[@class="bottom"]/ul/li | //div[@class="bottom"]/ul/div[2]/li')
    for a in a_list:
        city_name = a.xpath('./a/text()')[0]
        all_city_name.append(city_name)
    print(all_city_name)
    print ('Total: '+str(len(all_city_name)))
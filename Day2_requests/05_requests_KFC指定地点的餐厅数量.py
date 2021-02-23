# -*- coding:utf-8 -*-
import requests
import json

if __name__ == '__main__':
    post_url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
    }
    word = input('请输入地址：')
    params = {
        'cname': word,
        'pid': '',
        'pageIndex': '1',
        'pageSize': '10',
    }

    response = requests.post(url=post_url, data=params, headers=headers)
    page_text = response.text
    page_text_dic = eval(page_text)

    row_count = page_text_dic['Table']
    table = row_count[0]
    store_number = table['rowcount']

    fileName1 = 'Result05_kfc.json'
    with open(fileName1, 'w', encoding='utf-8') as fp:
        fp.write(page_text)

    print('在 %s 总共有 %d 家KFC门店。' %(word,store_number))

# -*- coding:utf-8 -*-
#需求：爬取糗事百科中糗图板块下所有的糗图图片

import requests

if __name__ == '__main__':
    #如何爬取图片数据
    url = 'https://pic.qiushibaike.com/system/pictures/12407/124076209/medium/8OMHP4SFO40VAIRX.jpg'

    #text (string) content(二进制) json() (对象)
    img_data = requests.get(url=url).content
    with open('./01_image.jpg','wb') as fp:
        fp.write(img_data)
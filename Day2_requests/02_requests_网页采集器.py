#- 需求：爬取搜狗制定词条对应的搜索结果页面（简易网页采集器）
# UA(User-Agent)伪装：门户网站的服务器会检测对应请求的载体，身份标识，如果检测到请求的载体，设备标识为某一款浏览器,说明该请求是一个正常的请求，
# 但是如果检测到请求的载体身份标识，不是基于某一款浏览器的，则表示该请求为不正常的请求。（爬虫）
#则服务器端可能拒绝访问
#UA(User_Agent)伪装: 让爬虫对应的请求载体身份标识伪装成某一款浏览器.

import requests
if __name__ == '__main__':
    #UA伪装：将对应的User-Agent封装到一个字典里
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
    }

    url = 'https://www.sogou.com/web'
    #处理url携带的参数：封装到字典中
    kw = input('Enter a word: ')
    param = {
        'query':kw
    }
    #对指定的url发起的请求对应的url时携带参数的，并且请求过程中处理了参数
    response = requests.get(url=url, params=param, headers=headers)
    page_text = response.text
    fileName = 'Result02_' + kw + '.html'
    with open(fileName, 'w', encoding='utf-8') as fp:
        fp.write(page_text)
    print(fileName, '保存成功！！')
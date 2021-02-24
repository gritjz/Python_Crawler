#反爬机制：封ip
#策略：使用代理ip请求发送
import requests
from lxml import etree

if __name__ == '__main__':
    url='https://www.baidu.com/s?wd=ip'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
    }
    #请求先发送到proxy
    page_text = requests.get(url=url, headers=headers, proxies={'https': 'https://183.166.111.107:9999'}).text

    with open('./3_ip.html', 'w', encoding='utf-8') as fp:
        fp.write(page_text)









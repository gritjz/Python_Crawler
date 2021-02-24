import requests
from lxml import etree
import json

# 1-对携带验证码的页面数据进行抓取
url = 'https://epass.icbc.com.cn/regist/regist_index.jsp?StructCode=1'
agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
headers = {
    'User-Agent': agent,
}
proxy = {
    "http": "121.8.98.196:80",
}
page_text = request.get(url=url, proxies=proxy, headers=headers).text

# 2-可以将页面数据中验证码进行解析，验证码图片下载到本地
tree = etree.HTML(page_text)
codeImg_url = tree.xpath('//*[@id="captcha_image"]/@src')[0]
# 获取 了验证码图片对应的二进制数据值
code_img = requests.get(url=codeImg_url, headers=headers).content

# 获取captcha-id
'<img id="captcha_image" src="https://www.douban.com/misc/captcha?id=Adc4WXGyiRuVJrP9q15mqIrt:en&size=s" alt="captcha" class="captcha_image">'
c_id = re.findall('<img id="captcha_image".*?id=(.*?)&amp.*?>', page_text, re.S)[0]  # 获取img中id的值
with open('./code.png', 'wb') as fp:
    fp.write(code_img)
# 获得了验证码图片上面的数据值
codeText = getCode('./code.png')
# 进行登录操作
post = 'https://accounts.douban.com/login'
data = {
    'source': 'movie',
    'redir': 'https://movie.douban.com/',
    'form_email': '15027900535',
    'form_password': 'bobo@15027900535',
    'captcha-solution': codeText,
    'captcha-id': c_id,
    'login': '登录',
}
login_text = requests.post(url=post, data=data, headers=headers).text
with open('./login.html', 'w', encoding='utf-8') as fp:
    fp.write(login_text)

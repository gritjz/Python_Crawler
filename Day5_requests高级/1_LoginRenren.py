# Procedure:
#1. 获取验证码图片文字数据
#2. 对post请求进行发送
#3. 对响应数据持久化储存

from CodeClass import YDMHttp
import requests
from lxml import etree

if __name__ == '__main__':

    def getCode(codeImg):
        # 云打码平台普通用户的用户名
        username = '用户'

        # 云打码平台普通用户的密码
        password = '密码'

        # 软件ＩＤ，开发者分成必要参数。登录开发者后台【我的软件】获得！
        appid = 6003

        # 软件密钥，开发者分成必要参数。登录开发者后台【我的软件】获得！
        appkey = 'xxxxxxxxxxx'

        # 验证码图片文件
        filename = codeImg

        # 验证码类型，# 例：1004表示4位字母数字，不同类型收费不同。请准确填写，否则影响识别率。在此查询所有类型 http://www.yundama.com/price.html
        codetype = 3000

        # 超时时间，秒
        timeout = 20

        # 检查
        if (username == 'username'):
            print('请设置好相关参数再测试')
        else:
            # 初始化
            yundama = YDMHttp(username, password, appid, appkey)

            # 登陆云打码
            uid = yundama.login();
            print('uid: %s' % uid)

            # 查询余额
            balance = yundama.balance();
            print('balance: %s' % balance)

            # 开始识别，图片路径，验证码类型ID，超时时间（秒），识别结果
            cid, result = yundama.decode(filename, codetype, timeout);
            print('cid: %s, result: %s' % (cid, result))

            return result


    url = 'http://www.renren.com/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
    }
    page_text = requests.get(url=url, headers=headers)
    tree = etree.HTML(page_text)
    code_img_src = tree.xpath('//*[@id="login"]/@src')[0]
    code_img_data = requests.get(url=code_img_src, headers=headers).content

    with open('./code.jpg', 'wb') as fp:
        fp.write(code_img_data)
    result = getCode('./code.jpg', 2004)

    #Post
    login_url = 'http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=202112213102'
    data={
        'email': '490541044@qq.com',
        'icode': result,
        'origURL': 'http: // www.renren.com / home',
        'domain': 'renren.com',
        'key_id': '1',
        'captcha_type': 'web_login',
        'password': '31fbd7f3ece9fce36d6923f7443ef59b88de676441a7f700ff78630aa26d1d72',
        'rkey': 'fa647ac3744264c8eece684183c36fe5',
        'f':'',
    }
    login_text = requests.post(url=login_url, data=data, headers=headers).text
    with open('./renrenlogin.html', 'w', encoding='utf-8') as fp:
        fp.write(login_text)
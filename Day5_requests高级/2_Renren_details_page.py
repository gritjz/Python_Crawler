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

    #创建一个session对象
    session = requests.Session();
    #模拟登录
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
    #使用session进行post请求的发送

    login_text = session.post(url=login_url, data=data, headers=headers).text
    with open('./renrenlogin.html', 'w', encoding='utf-8') as fp:
        fp.write(login_text)

    #------------------
    details_url='http://www.renren.com/334479447/profile'


    #手动处理cookie
    #
    # headers={
    #     'Cookie':'anonymid=klirsr9iexywjj; depovince=GW; _r01_=1; JSESSIONID=abcsMFu5b7CbOaZivSrFx; taihe_bi_sdk_uid=0e91d34189d5cbc51dffca912b0f2d61; taihe_bi_sdk_session=0a95310754520b64c21745d20c7c25aa; ick_login=44b3ee1a-7574-493f-9f51-fe88b6c37d3d; first_login_flag=1; ln_uact=490541044@qq.com; ln_hurl=http://hdn.xnimg.cn/photos/hdn521/20100812/1405/h_main_Jh3j_1f5f0001ede72f76.jpg; wp_fold=0; jebecookies=7b195dc1-12b6-4b1b-bf7e-6b92edfd318c|||||; _de=9C2D021C57361FCF303554EBBEB4676C696BF75400CE19CC; p=65182b06b33bc556241ebf64558d89377; t=86de05f43a74fb092649b1c9fdac5d1a7; societyguester=86de05f43a74fb092649b1c9fdac5d1a7; id=334479447; xnsid=2e263764; ver=7.0; loginfrom=null'
    # }

    #自动处理cookie
    #使用携带cookie的session来进行get
    detail_page_text = session.get(url=details_url,headers=headers).text
    with open('./renrenDetails.html', 'w', encoding='utf-8') as fp:
        fp.write(detail_page_text)


























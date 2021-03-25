
import requests
import json
if __name__ == '__main__':
    #1 指定url
    post_url = 'https://fanyi.baidu.com/sug'
    #2 进行UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
    }
    #3 post请求参数处理
    word = input('enter a word: ')
    data = {'kw': word}

    #4 请求发送
    response = requests.post(url=post_url,data=data)
    #5 获取响应数据,json返回obj(如果确认响应数据时json类型的，才能使用json())
    dic_obj = response.json()

    #6持久化存储
    fileName = 'Result03_' + word + '.json'
    fp = open(fileName, 'w', encoding='utf-8')
    json.dump(dic_obj, fp, ensure_ascii=False)
    print('over')
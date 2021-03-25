# -*- coding:utf-8 -*-
import requests
import json

if __name__ == '__main__':
    url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
    }
    id_list = []
    all_data_list = []
    for page in range(1, 5):
        page = str(page)
        data = {
        'on': 'true',
        'page': page,
        'pageSize': '15',
        'productName': '',
        'conditionType': '1',
        'applyname': '',
        }
        json_ids = requests.post(url=url, headers=headers, data=data).json()
        for dic in json_ids['list']:
            id_list.append(dic['ID'])

    print(len(id_list))

    detail_url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
    for id in id_list:
        detail_data = {
            'id': id
        }
        result = requests.post(url=detail_url, headers=headers, data=detail_data).json()
        all_data_list.append(result)
        #print(id)

    fileName = 'Result06_makeup.json'
    fp = open(fileName, 'w', encoding='utf-8')
    json.dump(all_data_list, fp=fp, ensure_ascii=False)
    print('over!!')


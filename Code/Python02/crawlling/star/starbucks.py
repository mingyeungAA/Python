# -*- coding:utf-8 -*-

import requests
import json
from numpy.dual import det


# https://www.starbucks.co.kr/index.do -> STORE -> 매장찾기 -> 지역검색

def getSiDo():
    url = 'https://www.starbucks.co.kr/store/getSidoList.do'
    resp = requests.post(url)
    #print(resp.json())
    #print(resp.json()['list'])
    sido_json = resp.json()['list']
    sido_code = list(map(lambda x: x['sido_cd'], sido_json))
    #print(sido_code)
    sido_name = list(map(lambda x: x['sido_nm'], sido_json))
    #print(sido_name)
    sido_dict = dict(zip(sido_code, sido_name))
    #print(sido_dict)
    return sido_dict
    

def getGuGun(sido_code):
    url = 'https://www.starbucks.co.kr/store/getGugunList.do'
    resp = requests.post(url, data={'sido_cd' : sido_code})
    #print(resp.json())
    gugun_json = resp.json()['list']
    gugun_dict = dict(zip(list(map(lambda x: x['gugun_cd'], gugun_json)),list(map(lambda x: x['gugun_nm'], gugun_json))))
    #print(gugun_dict)
    return gugun_dict
    

def getStore(sido_code='', gugun_code=''):
    url = 'https://www.starbucks.co.kr/store/getStore.do'
    resp = requests.post(url, data={
                                                                'ins_lat ': '37.56682',
                                                                'ins_lng': '126.97865',
                                                                'p_sido_cd': sido_code,
                                                                'p_gugun_cd': gugun_code,
                                                                'in_biz_cd' : '',
                                                                'set_date' : ''
                                                                })
    #print(resp.json()['list'])
    # s_name, tel, doro_address, lat, lot -> json으로 만들자
    store_json = resp.json()['list']
    store_list = list()
    count = 0
    for store in store_json:
        store_dict = dict()
        store_dict['s_name'] = store['s_name']
        store_dict['tel'] = store['tel']
        store_dict['latitude'] = store['lat']
        store_dict['longitude'] = store['lot']
        store_dict['doro_address'] = store['doro_address']
        #print(store_dict)
        store_list.append(store_dict)
        count+=1
    #print(count)
    store_result = dict()
    store_result['store_list'] = store_list
    store_result['count'] = count
    result = json.dumps(store_result, ensure_ascii=False)
    
    return result
    


if __name__ == '__main__':
    print(getSiDo())
    sido = input('도시 코드를 입력해 주세요 : ')
    if sido == '17':
        print(getStore(sido_code=17, gugun_code=1701))
    else:
        print(getGuGun(sido))
        gugun = input('구군 코드를 입력해주세요 : ')
        print(getStore(gugun_code=gugun))
    
    

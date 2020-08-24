# -*- coding:utf-8 -*-


from bs4 import BeautifulSoup
import requests
import json


resp = requests.get('https://comic.naver.com/webtoon/weekdayList.nhn?week=mon')
soup = BeautifulSoup(resp.text, 'html.parser')

#print(soup)

webtoons = soup.find_all('dl')
#print(webtoons)
#print(webtoons[0])


#제목이랑 별점 출력하자.
'''
for webtoon in webtoons:
    title = webtoon.find('a').text
    star = webtoon.find('strong').text
    print('{} [{}]'.format(title, star))
'''

#아래는 쌤이 하신거
webtoons = soup.find('ul', {'class': 'img_list'})
#print(webtoons)

dl = webtoons.select('dl')

lst = list()

for chd in dl:
    title = chd.find('a').text
    star = chd.find('strong').text
    #print('{} [{}]'.format(title, star))
    tmp = {}
    tmp['title'] = title
    tmp['star'] = star
    lst.append(tmp)
#print(lst) : [{}, {}, ,,,,{}] : json이 아님

# ↓json으로 만드는과정↓
res = {}   
res['webtoons'] = lst   #key가 webtoons 가 됨
#print(res)  :  {'webtoons' : [{},{}...{}]}

res_json = json.dumps(res, ensure_ascii=False)
print(res_json)     #더블쿼테이션 딕셔너리로 만들어짐

with open('webtoons.json', 'w', encoding='utf-8') as f:
    f.write(res_json)



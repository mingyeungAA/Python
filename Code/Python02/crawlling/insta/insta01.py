# -*- coding:utf-8 -*-


from bs4 import BeautifulSoup
import requests


tag = input('search keyword : ')
url = 'https://www.instagram.com/explore/tags/' + tag

resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'html.parser')
#print(soup)

res = soup.find('div', {'class': 'KL4Bh'})
print(res)


# -*- coding:utf-8 -*-


from bs4 import BeautifulSoup
#파이썬 기본 라이브러리 (내가 원하는 페이지랑 연결 가능)
import urllib.request


resp = urllib.request.urlopen('https://movie.naver.com/movie/running/current.nhn#')
#print(resp)

soup = BeautifulSoup(resp, 'html.parser')
#print(soup)


movies= soup.find_all('dl', class_='lst_dsc')
#print(movies)
#print(movies[0])


# 제목과 별점만 출력하자.
for movie in movies:
    title = movie.find('a').text    # find : 제일 위에 있는 a태그만 찾을거다
    star = movie.find('span', class_='num').text
    print('{} [{}]'.format(title, star))

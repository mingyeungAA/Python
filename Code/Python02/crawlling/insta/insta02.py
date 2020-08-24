# -*- coding:utf-8 -*-

from selenium import webdriver
from bs4 import BeautifulSoup


url = 'https://www.instagram.com/explore/tags/' + input('search keyword: ')

driver = webdriver.Chrome('C:/test/chromedriver.exe')
driver.implicitly_wait(3)
driver.get(url)

soup = BeautifulSoup(driver.page_source, 'html.parser')
img_list = soup.find_all('div' ,{'class' : 'KL4Bh'})
print(img_list)



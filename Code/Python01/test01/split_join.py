# -*- coding:utf-8 -*-

# [] : list
# {} : set, dictionary
# () : tuple

## split
str01 = 'Hello, World!\nHello, Python!'
print(str01)

arr01 = str01.split(' ')    #공백으로 자르자
print(arr01)

arr02 = str01.split(' ', 2)   #maxsplit 최대 몇개로 잘라주세여(공백을 최대 2개로 잘라주세여)
print(arr02)


import re    #맨위에 써도 됨(필요한 부분에다가 써둬도 됨)
arr03 = re.split("[\s]|[,]", str01)    #정규식
print(arr03)


## join
arr04 = ['1','2','3','4']
print(arr04)
a='+'.join(arr04)
print(a)
print(eval(a))    #eval은 웬만하면 쓰지 말자!


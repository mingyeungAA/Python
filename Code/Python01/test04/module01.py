# -*- coding:utf-8 -*-

# math라는 module을 가져온다.
#import math

# module에서 내가 원하는 것만 가져올수있다.
from math import  pi

def circle(r):
    # pi * r * r    
    return pi*r*r



if __name__ == '__main__':
    r = int(input('원의 반지름 : '))
    print('반지름이 {}인 원의 넓이는 {} 입니다.'.format(r, circle(r)))
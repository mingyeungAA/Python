# -*- coding:utf-8 -*-

import random
#중복이 안되고 순서가 없다. = set

# 1부터 45사이의 숫자 6개를 중복 없이 만들어서 리스트로 리턴하는 lotto() 함수를 만들자.
# main함수에서 호출하여 출력하자.

def lotto():
    lotto = set()
    
    while len(lotto) <= 6:
        ran = random.randint(1, 45)
        lotto.add(ran)
        
    result = sorted(lotto)
    print(result)


if __name__ == '__main__':
    print(lotto())


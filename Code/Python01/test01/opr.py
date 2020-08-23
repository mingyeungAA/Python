# -*- coding:utf-8 -*-


## 산술연산
a=21
b=2
print(a+b)
print(a-b)
print(a*b)
print(a ** b)     #a의 b제곱
print(a/b)
print(a // b)     # 나누고 나머지 제거 (=몫) (floor division - 소수점 이하는 버린다.)
print(a%b)      # 나머지 (modulo)

print("===============")

## 비교 연산
a,b = 3,5
print(a == b)
print(a != b)
print(a > b)
print(a  <= b)
print(a is b)
print(a is not b)

print("---------")
print(True or False)
print(False and True)
print(not False)


print("===============")

## 범위 연산
lst = list(range(100))    #0~99 까지
print(lst)
print(lst[2])
print(lst[12:49])    #12~48 까지
print(lst[12:49:3])    #12~48 까지 3씩 뛰어넘어서 출력
#[start : end]  ->  start~end-1
#[start : end : step]  ->  start~end-1 까지 step만큼 뛰면서 


str01 = 'Hello World!'    #list 순서가 있는
print(str01)
print(str01[0])
print(str01[0:5])
print(str01[6:11])
print(str01[0:4]*4)


## reverse
print(str01[-1])
print(str01[-1: ])
print(str01[:-1])
print(str01[::-1])



## 멤버연산
lst02 = [0,1,2,3,4,5]
print(3 in lst02)
print(5 not in lst02)
print(7 not in lst02)




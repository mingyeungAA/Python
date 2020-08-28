# -*- coding:utf-8 -*-


# n! = n * (n-1) * (n-2) * ... * 2 * 1

#for문 사용
def factorial(n):
    res=1
    for i in range(1, n+1):
        res*=i 
    return res


#재귀함수
def factorialREcursion(n):
    #종료조건
    if n ==1:
        return 1
    
    return n * factorialREcursion(n-1)


if __name__ == '__main__':
    n = int(input('input n : '))
    print('{} factorial = {}'.format(n, factorial(n)))
    print('{} factorial = {}'.format(n, factorialREcursion(n)))




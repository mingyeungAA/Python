# -*- coding:utf-8 -*-

# # 1. for문을 사용하여 구구단을 전체 출력하는 함수 gugu()를 작성하고, main함수에서 호출하자.
# # 2. while문을 사용하여 구구단 중 파라미터로 전달된 단만 출력하는 gugudan(x)를 작성하고, main함수에서 콘솔을 통해 n을 입력받아 호출하자.


def gugu():
    for i in range(2, 10):
        print('<<' + str(i) + "단>>")
        for j in range(1, 10):
            print(str(i) + '*' + str(j) + ' = ' , i * j)
        print()


def gugudan(x):
  i = 1
  while i < 10:
      print('{} * {} = {}'.format(x, i, int(x) * i))
      i += 1
  print()


if __name__ == '__main__':
    print(gugu())
    print('-----------')
    n = input('dan : ')
    gugudan(n)

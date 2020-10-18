from pandas_datareader import data as pdr
from pandas import Series, DataFrame
import yfinance as yf
from datetime import datetime
import unittest

start = datetime(2020,4,17)
end = datetime(2020,10,17)

#6개월동안의 apple사 주식 정보 알려줌
apple = pdr.DataReader("AAPL", "yahoo", start, end)
#print(apple)

#apple사의 'Close'항목만 나열된다.
#print(apple['Close'])

#apple사의 date항목만 출력됨
#print(apple.index)


# 반복문 돌려서 apple_data에 apple['Close'] 넣기
#Series에 넣기!
apple_close = Series(apple['Close'])
#print(apple_close)
#print(apple_close[4])

# 날짜를 모두 apple_date에 넣음
apple_date = Series(apple.index)
#print(apple_date[1])

#apple_data라는 변수에 'Close'의 정보와 날짜를 넣음
apple_data =Series(apple_close, index=apple_date) 
#print(apple_data[apple_close])  #close값만 쭉 나열됨
apple_data.index.name='Date'
#print(apple_data.index)
#print(apple_data['67.08749389648438'])
#print(apple_data['2020-10-15'])

###################
# DataFrame으로 만들기
apple_day = DataFrame(apple_close, index=apple_date)
#print(apple_day)
print("##")
print(apple_day['Close'].index)
#print(apple_close[2])   #69.232498..


# 날짜로 Close값을 검색할때
day_data = apple_day.loc['2020-10-16']
#print(day_data)  #Close 119.019997 라고 출력됨.
###################

# 최대수익 알고리즘
def max_profit(prices):
    n = len(prices)
    max_profit = 0
    min_price = prices[0]

    for i in range(1, n):
        profit = prices[i]-min_price

        if profit > max_profit:
            max_profit = profit
        if prices[i] < min_price:
            min_price = prices[i]

    return max_profit


# 해당 주가의 날짜 출력하기
# apple_data.index(날짜부분)


# 최대수익과 날짜 출력하기
print(max_profit(apple_close))   #67.0874938..
#print(date(max_profit(apple_close)))

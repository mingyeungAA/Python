from pandas_datareader import data as pdr
from pandas import Series, DataFrame
import yfinance as yf
from datetime import datetime
import pandas as pd

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
apple_close = Series(apple['Close'])
#print(apple_close[4])

# 날짜를 모두 apple_date에 넣음
apple_date = Series(apple.index)
#print(apple_date[1])

#apple_data라는 변수에 'Close'의 정보와 날짜를 넣음
apple_data =Series(apple['Close'], index=apple_date) 
print(apple_data)

print(apple_data['2020-10-15'])
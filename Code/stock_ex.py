from pandas_datareader import data as pdr
from pandas import Series, DataFrame
from datetime import datetime


start = datetime(2020,4,17)
end = datetime(2020,10,17)

apple = pdr.DataReader("AAPL", "yahoo", start, end)


apple_close = Series(apple['Close'])


data = DataFrame(apple_close)


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

final_profit = max_profit(data['Close'])

print(final_profit)   

#최대수익을 내는 날짜 출력하기..
#구현 못함 ㅠㅠ
n=len(apple_close)
for i in range(n):
    if data['Close'][i]==final_profit:
        print(data['Close'][i].index)




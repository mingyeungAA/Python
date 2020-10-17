

def max_profit(prices):
    # n은 prices의 문자열 길이 
    n = len(prices)
    # 최대 수익은 항상 0이상의 값
    max_profit = 0
    # 첫째 날의 주가를 주가의 최솟값으로 기억
    min_price = prices[0]

    # 1부터 n-1까지 반복
    for i in range(1, n):
        #지금까지의 최솟값에 주식을 사서 i날에 팔때의 수익
        profit = prices[i] - min_price

        #이 수익이 지금까지 최대 수익보다 크면 값을 고침
        if profit > max_profit:
            max_profit = profit
        if prices[i] < min_price:
            min_price = prices[i]

    return max_profit

stock = [10300, 9600, 9800, 8200, 7800, 8300, 9500, 9800, 10200, 9500]
print(max_profit(stock))

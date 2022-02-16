def maxProfit(prices):
    curr_price = prices[0]
    profit = 0

    for price in prices:
        curr_price = min(price, curr_price)
        profit = max(profit, price - curr_price)
    return profit


print(maxProfit([7, 1, 5, 3, 6, 4]))

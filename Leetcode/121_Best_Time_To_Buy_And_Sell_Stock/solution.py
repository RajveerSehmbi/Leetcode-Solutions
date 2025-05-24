# Sliding Window O(n) 

profit = 0
buy_price = None
for i, price in enumerate(prices):
	if i == 0:
		buy_price = prices[i]
		continue
	
	sell_price = prices[i]
	profit = max(profit, sell_price - buy_price)
	if sell_price < buy_price:
		buy_price = sell_price
return profit

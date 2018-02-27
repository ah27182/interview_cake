# https://www.interviewcake.com/question/python/stock-price

# Solution
def get_max_profit(stock_prices):
	curr_min_price = stock_prices[0]
	max_profit = 0

	for p in stock_prices:
		curr_min_price = min(p, curr_min_price)
		max_profit = max(p - curr_min_price, max_profit)

	return max_profit

'''
Explanation
Iterate through array and keep two values: 
	- the current minimum stock value  
	- the maximum profit that can be attained at that period of time

At the end, the maximum profit is returned as the answer
'''	

stock_prices_yesterday = [10, 7, 5, 8, 11, 9]

print(get_max_profit(stock_prices_yesterday))
# Returns 6 (buying for $5 and selling for $11)

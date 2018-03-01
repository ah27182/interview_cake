'''
Solution:
Addapted from this link in Berkeley's CS 61a: 
http://composingprograms.com/pages/17-recursive-functions.html#example-partitions
'''

# Code
def count_change(amount, denominations):
	denominations.sort()
	return count_partitions(amount, denominations)

def count_partitions(amount, coins):
	if amount == 0:
		return 1

	elif amount < 1:
		return 0

	if not coins:
		return 0

	coin = coins.pop()

	return count_partitions(amount - coin, coins + [coin]) + count_partitions(amount, coins)
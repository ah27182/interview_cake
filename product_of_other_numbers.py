from functools import reduce
from collections import Counter

'''
Solution:
Create a counter for all numbers in list.
Apply the product function on each number, which does the following:
	- decrements the counter
	- determines the product of all numbers
	- increments  the counter
Return a list of products
'''

# Code
def get_products_of_all_ints_except_at_index(numbers):
	cnt = Counter()

	for i in numbers:
		cnt[i] += 1

	return [product(cnt, i) for i in numbers]


def product(cnt, num):

	cnt[num] -= 1
	prod = 1

	for number in cnt:
		prod *= number ** cnt[number]

	cnt[num] += 1

	return prod

print(get_products_of_all_ints_except_at_index([1, 7, 7, 3, 4]))
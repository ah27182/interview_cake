from functools import reduce
'''
Solution:
Simple sort the input array and retrieve the last 3 numbers, 
these will be the largest numbers to multiply making it the highest product
'''

# Code
def max_triple_product(list_of_ints):
	list_of_ints.sort()
	max_three = list_of_ints[-3:]

	return reduce(lambda x,y: x*y, max_three)


max_triple_product([1,2,3,4,5,6])
# Expect: 120 (4 * 5 * 6)
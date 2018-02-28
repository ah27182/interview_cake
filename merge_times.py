'''
Solution:
Sort meetings first, ensuring that mergeable times are adjacent to one another in the list.
Loop through each sequential pair
	- if mergeable, merge, delete extra, restart/break loop

And if there is no change to the list, return as all mergable timings have been merged.
'''

# Code
def merge_times(meetings):
	meetings.sort()

	while True:
		original_length = len(meetings)

		for i in range(len(meetings) - 1):
			times = meetings[i:i + 2]

			if mergeable(*times):
				meetings[i] = merge(*times)
				del meetings[i + 1]
				break

		if original_length == len(meetings):
			break


	return meetings

def mergeable(x,y):
	return min(x[1], y[1]) >= max(x[0], y[0])

def merge(x,y):
	return (min(x[0],y[0]), max(x[1],y[1]))

print(merge_times([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]))

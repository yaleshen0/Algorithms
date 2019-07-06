# Given an array of integers, return indices of the two numbers 
# such that they add up to a specific target.

# You may assume that each input would have exactly one solution, 
# and you may not use the same element twice.

# Example:

# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1]

def q2(array, X): # time complexity: O(n) using hashing
	two_sum_set = set()
	for i in range(len(array)):
		temp = X - array[i]
		if temp in two_sum_set:
			print(temp, X-temp)
		two_sum_set.add(array[i])

A = [1,4,45,6,10,8]
sum = 16
q2(A, 16)


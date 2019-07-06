# For example, if the array is 
# [3, 5, 2, -4, 8, 11] and the 
# sum is 7, your program should 
# return [[11, -4], [2, 5]]
# because 11 + -4 = 7 and 2 + 5 = 7.

array = [1,4,45,6,10,-8]
# def twoSum(arr, s):
# 	output = []
# 	for i in range(len(array)):
# 		for j in range(len(array)):
# 			if array[i] + array[j] == s:
# 				output.append([array[i], array[j]])
# 	return output

# def twoSum(arr, S):
# 	hashset = set()
# 	for i in range(0, len(arr)):
# 		diff = S - arr[i]
# 		if diff in hashset:
# 			print("pair of numbers add up %d:" %S, arr[i], diff)
# 		hashset.add(arr[i])

# twoSum(array, 16)
rlist = set()
rlist.add((0,1))
rlist.add((1,10))
print(rlist(1))
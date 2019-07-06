array = [0, -1, 2, -3, 1]
# def threeSum(arr, s):
# 	n = len(arr)
# 	found = True
# 	for i in range(0, n-2):
# 		for j in range(i+1, n-1):
# 			for k in range(i+2, n):
# 				if arr[i] + arr[j] + arr[k] == s:
# 					print("Triplets add up to %d:" %s, arr[i], arr[j], arr[k])
# 					found = True
# 	if found == False:
# 		print("Not exist")
# time complexity: O(n3)
# auxiliary space: O(1)

# Iterate through every element. for every element
# arr[i], we find a pair with sum = sum - arr[i]
# using hashing can be solved in O(n) and O(n2) in total

def threeSum(arr, s):
	n = len(arr)
	found = True
	for i in range(0, n-1):
		hashset = set()
		for j in range(i+1, n):
			# sum of the two = s - arr[j]
			diff = s - arr[i] - arr[j]
			if diff in hashset:
				print("Triplets add up to %d: " %s, arr[i], arr[j], diff)
			else:
				hashset.add(arr[j])
	if found == False:
		print("No triplets found")
# time complexity: O(n2)
# auxiliary space: O(n)

threeSum(array, 2)
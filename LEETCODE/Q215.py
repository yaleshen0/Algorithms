def kthLarge(arr, k):
	arr = set(arr)
	return list(arr)[-k]
inpu = [3,2,3,1,2,4,5,5,6]
print(kthLarge(inpu, 2))
class Solution(object):
	# 双指针两侧向中间移动
	# def twoSum(self, arr, target):
	# 	left, right = 0, len(arr)-1;
	# 	while(right > left):
	# 		if(arr[left] + arr[right] == target):
	# 			return([left+1,right+1])
	# 		elif(arr[left] + arr[right] > target):
	# 			right = right-1
	# 		else:
	# 			left = left-1
	# 	return -1

	# 用字典保存
	def twoSum(self, arr, target):
		num_dict = {}
		for i, num in enumerate(arr):
			if(target-arr[i] in num_dict):
				return([num_dict[target-num], i+1])
			num_dict[num] = i+1

numbers = [2,7,11,15]
target = 9
print(Solution().twoSum(numbers, target))
# Given an array nums of n integers where n > 1,  return an array output 
# such that output[i] is equal to the product of all the elements of nums except nums[i].
class Solution(object):
	def prodOfArray(self, nums):
		"""
		type nums: array of int
		rtypeL List[int]
		"""
		size = len(nums)
		arr = [1] * size
		left = 1
		for i in range(size-1):
			left *= nums[i]
			arr[i+1] *= left
		right = 1
		for i in range(size-1, 0, -1): 
			right *= nums[i]
			arr[i-1] *= right
		print(arr[2])
		return arr
nums = [1,2,3,4]
print(Solution().prodOfArray(nums))
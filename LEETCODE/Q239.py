k = 3
nums = [1,-1]
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        size = len(nums)
        arr = []
        if(size == 0):
        	return []
        elif(size==1):
        	return nums
        elif(size==2):
        	arr.append(max(nums[0],nums[1]))
        	arr.append(nums[1])
        	return arr
        else:
        	for i in range(2, size):
        		arr.append(max(nums[i],nums[i-1],nums[i-2]))
        return arr




# print(Solution().maxSlidingWindow(nums,k))
print(nums[0:4])
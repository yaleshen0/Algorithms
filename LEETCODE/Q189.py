class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        nums = nums[k+1:n] + nums[0:n-k]
        return nums
nums = [1,2,3,4,5,6,7]
k = 3
print(Solution().rotate(nums, k))
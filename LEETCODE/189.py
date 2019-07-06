class Solution(object):
    # def rotate(self, nums, k):
    # n = len(nums)
    #     for i in range(k):
    #         tmp  = nums[n-1]
    #         for j in range(n-1, -1, -1):
    #             nums[j] = nums[j-1]
    #         nums[0] = tmp
    #     return nums
    def rotate(self, nums, k):
        n = len(nums)
        k %= n
        nums = self.reverse(nums, 0, n-1)
        nums = nums[:k][::-1] + nums[k:n][::-1]
        return nums
    def reverse(self, nums, start, end):
        while(end > start):
            nums[end],nums[start] = nums[start],nums[end]
            end -= 1
            start += 1
        # for i in range(n//2):
        #     nums[i],nums[n-i-1] = nums[n-i-1], nums[i]
        return nums
nums = [1,2,3,4,5,6,7]
print(Solution().rotate(nums,3))
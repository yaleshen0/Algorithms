# Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).
# Note: The solution set must not contain duplicate subsets.
# Input: [1,2,2]
# Output:
# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ]

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        outer_list = []
        nums = sorted(nums)
        return self.subsethelper(0, nums, outer_list)
    def subsethelper(self, index, nums, outer_list, sub_list=[]):
        outer_list.append(sub_list[:])
        for i in range(index, len(nums)):
            if (i!=index and nums[i] == nums[i-1]): 
            #     sub_list.append(nums[i])
            #     self.subsethelper(i+1, nums, outer_list, sub_list)
            #     sub_list.pop()
            # else:
            #     if (nums[i] != nums[i-1]):
            #         sub_list.append(nums[i])
            #         self.subsethelper(i+1, nums, outer_list, sub_list)
            #         sub_list.pop()
                continue
            else:
                sub_list.append(nums[i])
                self.subsethelper(i+1, nums, outer_list, sub_list)
                sub_list.pop()
        return outer_list
nums= [1,2,2]
print(Solution().subsetsWithDup(nums))
# Solution().subsetsWithDup(nums)
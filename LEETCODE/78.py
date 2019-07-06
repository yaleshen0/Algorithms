# Given a set of distinct integers, nums, return all possible subsets (the power set).
# Note: The solution set must not contain duplicate subsets.

# constraints: no duplicate subsets
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        outer_list = []
        return self.subsetsHelper(0,outer_list, nums)
    # def subsetsHelp(self, outer_list, nums):
    #     if sub_list not in outer_list:
    #         outer_list.append(sub_list[:])
    #         return
    #     for i in range(len(nums)):
    #         choose
    #         sub_list.append(nums[i])
    #         explore
    #         self.subsetsHelper(outer_list, nums[(i+1):])
    #         unchoose
    #         sub_list.pop()
    #     return outer_list
    def subsetsHelper(self, index,outer_list, nums, sub_list = []):
        # sub_list = sub_list or []
        # if (index == n):
        #     print(sub_list)
        #     outer_list.append(sub_list[:])
        outer_list.append(sub_list[:])
        for i in range(index,len(nums)):
            # choose
            sub_list.append(nums[i])
            # explore
            self.subsetsHelper(i+1, outer_list, nums, sub_list)
            # unchoose
            sub_list.pop()
        return outer_list
nums= [1,2,3]
print(Solution().subsets(nums))
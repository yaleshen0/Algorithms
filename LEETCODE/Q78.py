# 题意：枚举所有子集。

# 解题思路：碰到这种问题，一律dfs
class Solution(object):
	# @param S, a list of integer
	# @return a list of lists of integer
	def subsets(self, nums):
		"""
		:type nums: List[int]
		:rtyle: List[List[int]]
		"""
		result =[[]]
		for num in sorted(nums):
			result += [item + [num] for item in result]
		return result
if __name__ == "__main__":
    print(Solution().subsets([1, 2, 3]))
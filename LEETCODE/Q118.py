# Input: 5
# Output:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]

class Solution(object):
	def generate(self, numRows):
		"""
		:type numRows: int
		:rtype List[List[int]]
		"""
		pascalArray = []
		for i in range(1,numRows+1):
			arr = [0]*(i)
			arr[0] = arr[i-1] = 1
			pascalArray.append(arr)
		# print(pascalArray)
		for i in range(2, numRows):
			for j in range(1,len(pascalArray[i])-1):
				pascalArray[i][j] = pascalArray[i-1][j-1] + pascalArray[i-1][j]
		return pascalArray

input = 5
print(Solution().generate(input))
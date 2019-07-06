# Write an efficient algorithm that searches for a value in an m x n matrix. 
# This matrix has the following properties:
# 0.Integers in each row are sorted in ascending from left to right.
# 1.Integers in each column are sorted in ascending from top to bottom.
matrix = [[1,4,7,11,15],
[2,5,8,12,19],
[3,6,9,16,22],
[10,13,14,17,24],
[18,21,23,26,30]]

# time complexity: O(m+n)
class Solution(object):
	def searchMatrix(self, matrix, target):
		y = len(matrix[0]) -1
		for x in range(len(matrix)):
			while y and matrix[x][y] > target:
				y -= 1
			if matrix[x][y] == target:
				return True
		return False
# time complexity: O(m * longn)
class Solution1(object):
	def searchMatrix(self, matrix, target):
		y = len(matrix[0]) - 1
		def binarySearch(nums, low, high):
			while low <= high:
				middle = (low + high) //2 
				if nums[middle] > target:
					high = middle -1 
				else:
					low = middle + 1
				return high
		for x in range(len(matrix)):
			y = binarySearch(matrix[x], 0, y)
			if matrix[x][y] == target:
				return True
		return False
target = 20
print(Solution1().searchMatrix(matrix, target))
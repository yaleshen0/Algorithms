# rotate matrix clockwise by 90 degree
from __future__ import print_function
# time: O(n^2)
# space: O(1)
# class Solution(object):
	# @param matrix, a list of lists of integers
	# @return a list of lists of integers
	# def rotate(self, matrix):
	# 	n = len(matrix)

		# anti-diagonal mirror
		# for i in range(n):
		# 	for j in range(n-i):
		# 		matrix[i][j], matrix[n-1-j][n-1-i] = matrix[n-1-j][n-1-i], matrix[i][j]

		# horizontal mirror
		# for i in range(n//2):
		# 	for j in range(n):
		# 		matrix[i][j], matrix[n-1-i][j] = matrix[n-1-i][j], matrix[i][j]

		# return matrix 
# time: O(n^2)
# space: O(n^2)
class Solution2(object):
	# @param matrix, a list of lists of integers
	# @return a list of lists of integers
	def rotate(self, matrix):
		return [list(reversed(x) for x in zip(*matrix))]
if __name__ == "__main__":
	matrix = [[1,2,3],[4,5,6],[7,8,9]]
	print(Solution2().rotate(matrix))
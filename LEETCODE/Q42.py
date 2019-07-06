# Trapping rain water
class Solution(object):
	def trap(self, heights):
		if not heights or len(heights) < 3:
			return 0
		size = len(heights)
		lBound = [0] * size
		rBound = [0] * size

		h = heights[0]
		for i in range(size):
			lBound[i] = h = max(h, heights[i])

		h = heights[size-1]
		for i in reversed(range(size)):
			rBound[i] = h = max(h, heights[i])
		water = 0
		for i in range(size):
			water += min(lBound[i], rBound[i]) - heights[i]

		return water

if __name__ == "__main__":
	eleMap = [0,1,0,2,1,0,1,3,2,1,2,1]
	print(Solution().trap(eleMap))
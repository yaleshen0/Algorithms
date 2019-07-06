class Solution:
	# @param s, a string
	# @param dict, a set of string
	# @return a boolean
	def wordBreak(self, s, dicti):
		dp = [False for i in range(len(s) + 1)]
		dp[0] = True
		for i in range(1, len(s)+1):
			for k in range(i):
				if dp[k] and s[k:i] in dicti:
					dp[i] = True
		return dp[len(s)]
if __name__ == '__main__':
	s = 'leetcode'
	dicti = {'leet','code'}
	Solution().wordBreak(s, dicti)
# Given a string, find the first non-repeating character in it and 
# return it's index. If it doesn't exist, return -1.
from collections import Counter
from collections import defaultdict
class Solution(object):
	def firstUniStr(self, string):
		d = defaultdict(int)
		for s in string:
			d[s] += 1
		for u,v in d.items():
			if v==1:
				return string.find(u)
string = 'loveleetcode'
print(Solution().firstUniStr(string))
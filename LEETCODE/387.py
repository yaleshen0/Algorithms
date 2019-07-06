# s = "leetcode"
# return 0.

# s = "loveleetcode",
# return 2.
# class Solution(object):
#     def firstUniqChar(self, s):
"""
        :type s: str
        :rtype: int
        """
        # n = len(s)
        # dic = {}
        # if n == 1: return 0
        # for i in range(n):
        #     if ord(s[i]) not in dic.keys():
        #         dic[ord(s[i])] = 1
        #     else:
        #         dic[ord(s[i])] += 1
        # for i in range(n):
        #     if dic[ord(s[i])] == 1:
        #         return i
        # return -1


class Solution(object):
    def firstUniqChar(self, s):
        alp, ans = 'abcdefghijklmnopqrstuvwxyz', float('inf')
        for c in alp:
            i = s.find(c)
            if i == -1:
                continue
            j = s.find(c, i+1)
            if j == -1:
                ans = min(ans, i)
        if ans == float('inf'):
            return -1
        else:
            return ans
# string = "leetcode"
string = "aadadaad"      
# string = "loveleetcode"
print(Solution().firstUniqChar(string))
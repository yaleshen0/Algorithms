class Solution(object):
    # :type s: str e.x: "cbaebabacd"
    # :type p: str e.x: "abc"
    # :rtype: List[int]
    def findAnagrams(self, s, p):
        n = len(s) # length of string
        m = len(p) # length of pattern
        if (n==0 or m == 0 or n < m): return []
        res = [] # initialize output list
        dp = [0] * 26
        flag = 0
        j = 0
        for i in range(m):
            j = ord(p[i]) - 97
            dp[j] += 1
            if (dp[j] == 1): flag += 1
        for i in range(0, m):
            j = ord(s[i]) - 97
            dp[j] -= 1
            if dp[j] == 0: flag -= 1
            elif (dp[j] == -1): flag +=1
        print(flag)
        if flag ==0: res.append(0)
        for i in range(m, n):
            j = ord(s[i]) - 97
            dp[j] -= 1
            if dp[j] ==0: flag -= 1
            elif (dp[j] == -1): flag +=1
            # print(flag)
            j = ord(s[i - m]) - 97
            dp[j] += 1
            if (dp[j] == 0): flag -= 1
            elif (dp[j] == 1): flag += 1
            if( flag == 0):
                res.append(i - m + 1)
        return res
# s = 'cbaebabacd'
s = 'abae'
p = 'abc'

print(Solution().findAnagrams(s,p))
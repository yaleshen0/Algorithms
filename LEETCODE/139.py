# Input: s = "leetcode", wordDict = ["leet", "code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        # """
        # n = len(s)
        # output = {}
        # dic_set = set()
        # for i in wordDict:
        #     dic_set.add(i)
        # output[""] = True
        # for i in range(1,n+1):
        #     for j in range(i):
        #         if output.get(s[:j]) == True and s[j:i] in wordDict:
        #             output[s[:i]] = True
        # return output.get(s)
# class Solution(object):
#     def wordBreak(self, s, wordDict):
    #     return self.breakw(s,wordDict)
    # def breakw(self, s, d):
    #     dd = set()
    #     n = len(s)
    #     for w in d:
    #         if w in s:
    #             dd.add(w)
    #     dp = [False for i in range(len(s)+1)]
    #     dp[0] = True
    #     for i in range(1, n+1):
    #         for w in dd:
    #             print(s[i-len(w):i])
                # print(s[i-len(w):i])
        
# class Solution(object):
#     def wordBreak(self, s, wordDict):
        n = len(s)
        dp = [False for i in range(n+1)]
        dp[0] = True
        dic_set = set()
        maxLen = -1
        for i in wordDict:
            dic_set.add(i)
            maxLen = max(maxLen, len(i))
        print(maxLen)
        for i in range(1,n+1):
            for j in range(i):
                if dp[j] and s[j:i] in dic_set:
                    dp[i] = True
                    break
        return dp[n]
Input = "leetcode"
wordDict = ["leet", "code"]
# print("" in wordDict)
print(Solution().wordBreak(Input, wordDict))
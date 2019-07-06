# 344. Reverse String
# Input: ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        n = len(s)
        for i in range(n//2):
            s[i],s[n-i-1] = s[n-i-1],s[i]
        return s
test_input =  ["h","e","l","l","o"]
print(Solution().reverseString(test_input))
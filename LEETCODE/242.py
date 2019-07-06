class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        for i in range(ord('a'), ord('n')+1):
            c = chr(i)
            print(c)
            if s.count(c) != t.count(c):
                return False

        return True
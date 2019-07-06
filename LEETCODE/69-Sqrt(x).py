import math
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        return math.trunc(math.sqrt(x))

input = 8
print(Solution().mySqrt(input))
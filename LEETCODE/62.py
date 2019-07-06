# class Solution(object):
#     def uniquePaths(self, m, n):
"""
        :type m: int
        :type n: int
        :rtype: int
        """
        # uniquePaths(m, n) = uniquePaths(m - 1, n) + uniquePaths(m, n - 1)
    #     return self.uniquePathsHelper(m, n)
    # def uniquePathsHelper(self,m, n):
        # subUP = {}
        # if m == 1 or n == 1: return 1
        # mUP = subUP.get((m - 1, n), None)
        # nUP = subUP.get((m, n - 1), None)
        
        # if mUP and nUP: ans = mUP + nUP
        # elif mUP: ans = mUP + self.uniquePathsHelper(m, n - 1)
        # elif nUP: ans = nUP + self.uniquePathsHelper(m - 1, n)
        # else: ans = self.uniquePathsHelper(m, n - 1) + self.uniquePathsHelper(m - 1, n)
        
        # subUP[(m, n)] = ans
        # return ans
class Solution(object):
    def uniquePaths(self, m, n):
        total_path = [[1] * m] * n
        for i in range(1,n):
            for j in range(1,m):
                total_path[i][j] = total_path[i-1][j] + total_path[i][j-1]
                # print((i,j), total_path[i][j])
        return total_path[n-1][m-1]
print(Solution().uniquePaths(7,3))
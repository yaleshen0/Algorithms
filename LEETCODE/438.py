# class Solution(object):
#     def isAnagram(self, s1, s2):
#         return sorted(s1) == sorted(s2)
#     def findAnagrams(self, s, p):
#         """
#         :type s: str e.x: "cbaebabacd"
#         :type p: str e.x: "abc"
#         :rtype: List[int]
#         """
#         len1 = len(s) # 10
#         len2 = len(p) # 3
#         output_list = []
#         for i in range(len1-len2+1):
#             if self.isAnagram(s[i:i+(len2)], p):
#                 output_list.append(i)
#         return output_list
#! time limit exceeded
import time
start_time = time.time()
# class Solution(object):
#     def compare(self, arr1, arr2): 
#         for i in range(26):
#             if(arr1[i] != arr2[i]):
#                 return False
#         return True
    # def findAnagrams(self, s, p):
        """
        :type s: str e.x: "cbaebabacd"
        :type p: str e.x: "abc"
        :rtype: List[int]
        """
        # n = len(s) # length of txt
        # m = len(p) # length of pattern
        # outer_list = [] # initialize output list
        # if n < m: return []
        # arr1_counts = [0] * 26
        # arr2_counts = [0] * 26
        # for i in range(m):
            # print(arr1_counts[ord(s[i])])
            # arr1_counts[ord(s[i])-97] += 1
            # arr2_counts[ord(p[i])-97] += 1
        # arr1_counts = {ord(x): s[:m].count(x) for x in s[:m]}
        # arr2_counts = {ord(x): p.count(x) for x in p}
        # for i in range(m, n):
        #     if self.compare(arr1_counts, arr2_counts):
        #         outer_list.append(i-m)
            # from m digits on, count and uncount the letter and compare
            # arr1_counts[ord(s[i])-97] += 1 #if not exist, give 0 else += 1
            # arr1_counts[ord(s[i-m])-97] -= 1
            # k: x[k] for k in x if k in y and arr1_counts[k] == arr2_counts[k]
        # if (self.compare(arr1_counts, arr2_counts)):
        #     outer_list.append(i-m+1)
        # return outer_list
print(Solution().findAnagrams(s,p))
print("--- %s seconds ---" % (time.time() - start_time))
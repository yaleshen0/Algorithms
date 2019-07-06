class Solution(object):
    def combine(self, n, k):
        outer_list = []
        sub_list = []
        return self.combineHelper(1,n,k,outer_list,sub_list)
    def combineHelper(self,start,n,k,outer_list,sublist=None):
        # sublist = sublist or []
        if (len(sublist) == k):
            # print(sublist)
            outer_list.append(sublist[:])
            # print(outer_list)
            return
        else:
            for i in range(start, n+1):
                # choose
                sublist.append(i)
                # explore
                self.combineHelper(i+1, n,k,outer_list, sublist)
                #ub-choose
                sublist.pop()
        return outer_list
print(Solution().combine(4,2))
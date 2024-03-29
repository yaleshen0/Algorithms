# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """
class NestedIterator(object):
    
    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.__list = []
        self.__index = 0
        self.__getList(nestedList)
        
    def __getList(self, nestedList):
        for item in nestedList:
            if isinstance(item, int):
                self.__list.append(item.getInteger())
            else:
                self.__getList(item.getList())

    def next(self):
        """
        :rtype: int
        """
        res = self.__list[self.__index]
        self.__index += 1
        return res

    def hasNext(self):
        """
        :rtype: bool
        """
        if(self.__index < len(self.__list)):
            return True
        return False

nestedList = [[1,1],2,[1,1]]
# Your NestedIterator object will be instantiated and called as such:
i, v = NestedIterator(nestedList), []
while i.hasNext(): v.append(i.next())
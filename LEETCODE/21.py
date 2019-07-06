# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# class Solution(object):
# 	def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # newNode = ListNode(None)
        # dummyNode = newNode
        # if (l1 == None):
        #     return l2
        # if(l2 == None):
        #     return l1
        # while(l1 != None and l2 != None):
        #     if l2.val < l1.val:
        #         newNode.next = l2
        #         l2 = l2.next
        #     else:
        #         newNode.next = l1
        #         l1 = l1.next
        #     newNode = newNode.next
        # if (l1 == None or l2 == None):
        # 	newNode.next = l2 or l1
        # return dummyNode.next

class Solution(object):

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        if l1 == None and l2 == None:
            return None
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)
l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)
Node = Solution().mergeTwoLists(l1,l2)
# print(Node.val)
while(Node!=None):
	print(Node.val)
	Node = Node.next
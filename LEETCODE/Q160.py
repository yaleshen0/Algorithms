# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA:
        	return None
        if not headB:
        	return None
        newnode = ListNode(None)
        dummy = newnode
        while(headA and headB):
        	if(headA.val == headB.val):
        		dummy.next = ListNode(headA.val)
        		headA = headA.next
        		headB = headB.next
        return newnode.next

if __name__ == "__main__":
	headA = ListNode(1)
	headA.next = ListNode(2)
	headA.next.next = ListNode(3)
	headA.next.next.next  =ListNode(4)
	headA.next.next.next.next  =ListNode(5)
	headB = ListNode(5)
	headB.next = ListNode(6)
	headB.next.next = ListNode(3)
	headB.next.next.next  =ListNode(4)
	headB.next.next.next.next  =ListNode(5)
	solution = Solution()
	print(solution.getIntersectionNode(headA, headB))
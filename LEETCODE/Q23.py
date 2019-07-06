# import itertools
from queue import PriorityQueue
class ListNode(object):

	def __init__(self, val):
		self.val = val
		self.next = None

# class Solution(object):
# time complexity: O(NlogN)
# 	def mergeKLists(self,lists):
# 		"""
# 		:type lists: List[ListNode]
# 		:rtype: ListNode
# 		"""
# 		self.nodes = []
# 		head = point = ListNode(0)
# 		for l in lists:
# 			while l:
# 				self.nodes.append(l.val)
# 				l = l.next
# 		for i in sorted(self.nodes):
# 			point.next = ListNode(i)
# 			point = point.next
# 		return head.next

# optimized [compare one by one] using priority queue
# time complexity: O(NlogK) where k is # of lists
# class Solution2(object):
# 	def mergeKLists(self, lists):
# 		"""
# 		:type lists: List[ListNode]
# 		:rtype: ListNode
# 		"""
# 		head = point = ListNode(0)
# 		q = PriorityQueue()
# 		for l in lists:
# 			if l:
# 				q.put((l.val, l))

# 		while not q.empty():
# 			val, node = q.get()
# 			print(val)
# 			point.next = ListNode(val)
# 			point = point.next
# 			node = node.next
# 			if node:
# 				q.put((node.val, node))
# 		return head.next

# time: O(nlogk)
# space: O(logk)
# divide and conquer Solution
class Solution3:
	# @param a list of ListNode
	# @return a ListNode
	def mergeKLists(self, lists):
		def mergeTwoLists(l1,l2):
			head = point = ListNode(0)
			while l1 and l2:
				if(l1.val < l2.val):
					head.next = l1
					l1 = l1.next
				else:
					head.next = l2
					l2 = l2.next
				head = head.next
			head.next = l1 or l2
			return point.next

		def mergeKListsHelper(lists, begin, end):
			if(begin > end):
				return None
			if(begin == end):
				return lists[begin]
			return mergeTwoLists(mergeKListsHelper(lists, begin, (begin+end)/2),
									mergeKListsHelper(lists, (begin+end)/2+1, end))
		return mergeKListsHelper(lists, 0, len(lists) -1)

if __name__ == "__main__":
	l1 = ListNode(1)
	l1.next = ListNode(4)
	l1.next.next = ListNode(5)
	l2 = ListNode(1)
	l2.next = ListNode(3)
	l2.next.next = ListNode(4)
	l3 = ListNode(2)
	l3.next = ListNode(6)
	lists = [l1,l2,l3]
	print(Solution3().mergeKLists(lists))

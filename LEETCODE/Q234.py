class Node(object):
	def __init__(self, val):
		self.val = val
		self.next = None

# time complexcity: O(n)
# time space: O(n)
class Solution1(object):
	def isPalindrome(self, head):
		'''
		:type head: Node
		:rtype: bool
		'''
		if not head or not head.next:
			return True

		tem_list = []
		while head:
			tem_list.append(head.val)
			head = head.next

		length = len(tem_list)
		for i in range(0, length//2):
			if tem_list[i] != tem_list[length-i-1]:
				return False
		return True

# time complexcity: O(n)
# space complexcity: O(n/2)
# 将前半部分存入栈中 store first half into stack
# 出栈跟后半部分比较 and pop to compare with second half
class Solution2(object):
	def isPalindrome(self, head):
		'''
		:type head: Node
		:rtype: bool		
		'''
		if not head or not head.next:
			return True
		new_list =[]
		# 快慢指针找链表中点
		slow = fast = head
		while fast and fast.next:
			# store first half into stack
			new_list.insert(0, slow.val)
			slow = slow.next
			fast = fast.next.next
		if fast: # 链表有奇数个节点
			slow = slow.next
		
		print(new_list)
		for val in new_list:
			if val != slow.val:
				return False
				slow = slow.next
			return True
# time complexity: O(n)
# space complexity: O(1)
class Solution3(object):
	def isPalindrome(self, head):
		'''
		:type head: Node
		:rtype: bool		
		'''
		if not head or not head.next:
			return True

		# 快慢指针找链表中点
		slow = fast = head
		while fast.next and fast.next.next:
			slow = slow.next
			fast = fast.next.next
		slow = slow.next # slow 指向链表后半段
		slow = self.reverseList(slow)

		while slow:
			if head.val != slow.val:
				return False
			slow = slow.next
			head = head.next
		return True
	def reverseList(self, head):
		new_head = None
		while head:
			p = head
			head = head.next
			p.next = new_head
			new_head = p
		return new_head

head = Node(1)
head.next = Node(2)
head.next.next = Node(1)
head.next.next.next = Node(1)
# head.next.next.next.next = Node(1)
print(Solution3().isPalindrome(head))
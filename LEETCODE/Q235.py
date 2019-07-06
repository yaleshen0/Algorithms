class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.right = None
		self.left = None
class Solution(object):
	def lowestCommonAncestor(self, root, p, q):
		"""
		:type root: TreeNode
		:type p: TreeNode
		:type q: TreeNode
		:rtype: TreeNode
		"""
		if root == None:
			return None
		if (root.val > p) and (root.val > q):
			return self.lowestCommonAncestor(root.left, p, q)
		if (root.val < p) and (root.val < q):
			return self.lowestCommonAncestor(root.right, p, q)
		return root.val

root = TreeNode(6) 
root.left = TreeNode(2) 
root.right = TreeNode(8)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)
root.left.left = TreeNode(0) 
root.left.right = TreeNode(4) 
root.left.right.left = TreeNode(3) 
root.left.right.right = TreeNode(5)
n1 = 2
n2 = 8
n3 = 2
n4 = 4
t1 = Solution().lowestCommonAncestor(root, n1, n2)
t2 = Solution().lowestCommonAncestor(root, n3, n4)
print("lowest common ancestor between %d and %d is %d" %(n1,n2,t1))
print("lowest common ancestor between %d and %d is %d" %(n3,n4,t2))
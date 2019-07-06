# Invert a binary tree
# Method 1： DFS [递归： recursion]， for每个节点：交换左右子树 再对左右子树做同样操作
class TreeNode(object):
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None
class Solution(object):
	def invertTree(self, root):
		'''
		:type root TreeNode
		:rtype: TreeNode
		'''
		# base case
		if root == None:
			return root
		tmp = root.left
		root.left = self.invertTree(self, root.right)
		root.right = self.invertTree(self, tmp)
		return root

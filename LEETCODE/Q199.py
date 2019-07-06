# class Solution(object):
# 	def rightSideView(self, root):
# 		rightmost_val_at_depth = dict() # depth -> node.val
# 		max_depth = -1

# 		stack = [(root, 0)]
# 		while stack:
# 			node, depth = stack.pop()
# 			if node is not None:
# 				# maintain knowledge of the number of levels in the tree
# 				max_depth = max(max_depth, depth)

# 				# only insert into dict if depth is not already present.
# 				rightmost_val_at_depth.setdefault(depth, node.val)

# 				stack.append((node.left, depth+1))
# 				stack.append((node.right, depth+1))

# 		return [rightmost_val_at_depth[depth] for depth in range(max_depth+1)]

# cite geeksforgeeks
class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

# recursive func to print right view of binary tree used
# max_level as reference list .. only max_level[0] is helpful?
def rightViewUtil(root, level, max_level):
	# Base case
	if root is None: return

	# if this is the last node of its level
	if(max_level[0] < level):
		print("%d " %(root.data))
		max_level[0] = level

	# recur for right subtree first, then left subtree
	rightViewUtil(root.right, level+1, max_level)
	rightViewUtil(root.left, level+1, max_level)
# print view
def rightView(root):
	max_level = [0]
	rightViewUtil(root, 1, max_level)


# Driver program to test above function 
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5)
root.left.right.left = Node(9)
root.left.right.left.left = Node(10) 
root.right.left = Node(6) 
root.right.right = Node(7) 
root.right.left.right = Node(8) 
  
rightView(root) 
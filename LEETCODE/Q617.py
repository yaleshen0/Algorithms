# Input: 
# 	Tree 1                     Tree 2                  
#           1                         2                             
#          / \                       / \                            
#         3   2                     1   3                        
#        /                           \   \                      
#       5                             4   7                  
# Output: 
# Merged tree:
# 	     3
# 	    / \
# 	   4   5
# 	  / \   \ 
# 	 5   4   7
class Node(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
	def height(self,node): 
		if node is None:
			return 0
		else:
			# Compute the depth of each subtree 
			lheight = self.height(node.left) 
			rheight = self.height(node.right)
			# Use the larger one 
			if (lheight > rheight):
				return lheight+1
			else:
				return rheight+1
	def printLevelOrder(self,root):
	    h = self.height(root)
	    for i in range(1, h+1): 
	        self.printGivenLevel(root,i) 
	  
	  
	# Print nodes at a given level 
	def printGivenLevel(self,root , level): 
	    if root is None: 
	        return
	    if level == 1: 
	        print("%d" %(root.val)) 
	    elif level > 1 : 
	        self.printGivenLevel(root.left , level-1) 
	        self.printGivenLevel(root.right , level-1) 
	def mergeTrees(self, t1, t2):
		"""
    	:type t1: Node
    	:type t2: Node
    	:rtype: Node
    	"""
		if(t1==None):
			return t2
		if(t2==None):
			return t1
		t1.val += t2.val
		t1.left = self.mergeTrees(t1.left,t2.left)
		t1.right = self.mergeTrees(t1.right,t2.right)
		return t1
t1 = Node(1)
t1.left = Node(3)
t1.right = Node(2)
t1.left.left = Node(5)
t2 = Node(2)
t2.left = Node(1)
t2.right = Node(3)
t2.left.right = Node(4)
t2.right.right = Node(7)
solution = Solution()
root = solution.mergeTrees(t1, t2)
solution.printLevelOrder(root)